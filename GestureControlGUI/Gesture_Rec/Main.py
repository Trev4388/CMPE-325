# TechVidvan hand Gesture Recognizer

# import necessary packages

import cv2 #
import numpy as np # 
import mediapipe as mp #
import tensorflow as tf #
from tensorflow.keras.models import load_model #
import pyautogui as p  #pip install pyautogui

class GestureControl:
    def __init__(self,running = False):
        self.running = running
    def run(self):
        # initialize mediapipe
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        mpDraw = mp.solutions.drawing_utils

        # Load the gesture recognizer model
        model = load_model('Gesture_Rec/mp_hand_gesture')

        # Load class names
        f = open('Gesture_Rec/gesture.names', 'r')
        classNames = f.read().split('\n')
        f.close()
        print(classNames)

        PrevGesture = None
        alreadyDone = False
        stopped = False
        counter = 0
        workingGestures = ["peace - Skip Backward",
                           "fist - Decrease Volume",
                           "okay - Skip Forward",
                           "rock - Increase Volume",
                           "live long - Stop/Play",
                           "thumbs up - Increase Playback Speed",
                           "thumbs down - Decrease Playback Speed"]

        # Initialize the webcam
        cap = cv2.VideoCapture(0)
        while self.running:
            # Read each frame from the webcam
            _, frame = cap.read()

            x, y, c = frame.shape

            # Flip the frame vertically
            frame = cv2.flip(frame, 1)
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get hand landmark prediction
            result = hands.process(framergb)

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
                    mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS,
                                                mpDraw.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                                mpDraw.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                                 )  
        ##            # Predict gesture
                    prediction = model.predict([landmarks])
        ##            # print(prediction)
                    classID = np.argmax(prediction)
                    className = classNames[classID]
                    
            # show the prediction on the frame
                if className in workingGestures:
                    #print(counter, PrevGesture, className)
                    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                                   0.5, (0,0,255), 2, cv2.LINE_AA)
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
            cv2.imshow("Output", frame) 

            if cv2.waitKey(1) == ord('q'):
                self.running = False

        # release the webcam and destroy all active windows
        cap.release()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    gestureControl = GestureControl(True)
    gestureControl.run()