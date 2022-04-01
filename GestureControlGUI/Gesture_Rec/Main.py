# TechVidvan hand Gesture Recognizer

# import necessary packages

import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pyautogui as p  # pip install pyautogui
#from tensorflow.keras.models import load_model  #
from tensorflow.python.keras.models import load_model

class GestureControl:
    def __init__(self,running = False):
        self.running = running
        self.visual = True

        mpHands = mp.solutions.hands
        self.hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils
        # initialize mediapipe
       
        # Load the gesture recognizer model
        self.model = load_model('Gesture_Rec/mp_hand_gesture')

        # Load class names
        f = open('Gesture_Rec/gesture.names', 'r')
        self.classNames = f.read().split('\n')
        f.close()
        print(self.classNames)
        self.workingGestures = ["peace - Skip Backward",
                           "fist - Decrease Volume",
                           "okay - Skip Forward",
                           "rock - Increase Volume",
                           "live long - Stop/Play",
                           "thumbs up - Increase Playback Speed",
                           "thumbs down - Decrease Playback Speed"]

        # Initialize the webcam
    def run(self):
        cap = cv2.VideoCapture(0)
        PrevGesture = None
        alreadyDone = False
        stopped = False
        counter = 0
        while self.running:
            # Read each frame from the webcam
            _, frame = cap.read()

            x, y, c = frame.shape

            # Flip the frame vertically
            frame = cv2.flip(frame, 1)
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get hand landmark prediction
            result = self.hands.process(framergb)

            # print(result)
            
            className = ''

            # post process the result
            if result.multi_hand_landmarks:
                landmarks = []
                for handslms in result.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        # print(id, lm)
                        lmx = int(lm.x * x)
                        lmy = int(lm.y * y)

                        landmarks.append([lmx, lmy])

                    # Drawing landmarks on frames
                    self.mpDraw.draw_landmarks(frame, handslms, self.mpHands.HAND_CONNECTIONS,
                                                self.mpDraw.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                                self.mpDraw.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                                 )  
        ##            # Predict gesture
                    prediction = self.model.predict([landmarks])
        ##            # print(prediction)
                    classID = np.argmax(prediction)
                    className = self.classNames[classID]
                    
            # show the prediction on the frame
                if className in self.workingGestures:
                    #print(counter, PrevGesture, className)
                    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                                   0.5, (0,0,255), 1, cv2.LINE_AA)
                    if PrevGesture == className:
                        counter += 1
                    elif PrevGesture != className:
                        alreadyDone = False
                        counter = 0
                        PrevGesture = className

                if counter==5 and alreadyDone == False:
                    alreadyDone = True
                    if className == "okay - Skip Forward":
                        print("Skipped Forward")
                        p.press("right")
                        p.press("right")
                    elif className == "peace - Skip Backward":
                        print("Skipped Backward")
                        p.press("left")
                        p.press("left")
                    elif className == "rock - Increase Volume":
                        print("Increased Volume")
                        p.press("up")
                    elif className == "fist - Decrease Volume":
                        print("Decreased Volume")
                        p.press("down")
                    elif className == "live long - Stop/Play":
                        print("Stop/Play")
                        p.press("space")
                    elif className == "thumbs up - Increase Playback Speed":
                        print("Increase Playback Speed")
                        p.hotkey("shift",">")
                    elif className == "thumbs down - Decrease Playback Speed":
                        print("Decrease Playback Speed")
                        p.hotkey("shift","<")
            elif alreadyDone == True:
                alreadyDone = False
                counter = 0
            # Show the final output
            if self.visual:
                cv2.imshow("Output", frame) 

            if cv2.waitKey(1) == ord('q'):
                self.running = False

        # release the webcam and destroy all active windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    gestureControl = GestureControl(True)
    gestureControl.run()