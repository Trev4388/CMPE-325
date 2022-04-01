import PySimpleGUI as sg
from Gesture_Rec import Main
import threading


gestureControl = Main.GestureControl()
sg.theme("DarkBlue")

layoutLaunch = [[sg.Text("Welcome to the launch")],
                [sg.Text("Click to close")], [sg.Button("Stop")]]

# Create the window

windowLaunch = sg.Window("Gesture Control Launch", layoutLaunch, element_justification='c', size=(750,700))
# Create an event loop
heads = ["Welcome to the tutorial",
        "The next recognized gesture is called 'fist' and can be seen below:",
         "The next recognized gesture is called 'rock' and can be seen below:",
         "The next recognized gesture is called 'peace' and can be seen below:",
         "The next recognized gesture is called 'okay' and can be seen below:",
         "The next recognized gesture is called 'thumbs down' and can be seen below:",
         "The next recognized gesture is called 'thumbs up' and can be seen below:",
         "You have now learned all of the recognized gestures."]
text1s = ["The purpose of the tutorial is to demonstrate how to perform each recognized gesture and explain what each gesture does.",
        "The fist gesture is used to decrease the volume.",
        "The rock gesture is used to increase the volume.",
        "The peace gesture is used to skip backwards in a video.",
        "The okay gesture is used to skip forwards in a video.",
        "The thumbs down gesture is used to decrease playback speed in a video.",
        "The thumbs up gesture is used to increase playback speed in a video.",
        "You can now launch the gesture recognition system by clicking the 'Start' button below."]
text2s = ["The first recognized gesture is called 'live long' and can be seen below:",
        "Click the 'Next' button to view the next gesture",
        "Please make sure you have selected the tab in which the video is playing before attemting gestures.\n                                                     Press 'Q' to end gesture control."] #3
imgs = ["Images/live_long(pauseplay).png",
        "Images/fist(DecreaseVolume).png",
        "Images/rock(IncreaseVolume).png",
        "Images/peace(skipBack).png",
        "Images/okay(skipForwards).png",
        "Images/thumbsDown(DecSpeed).png",
        "Images/thumbsUp(IncSpeed).png",
        "Images/logo.png"]

def createwindow():
    layout = [[sg.Text(heads[0], key = "_head_", visible=True)],
          [sg.Text(text1s[0], key = "_text1_", visible=True)],
          [sg.Text(text2s[0], key = "_text2_", visible=True)],
          [sg.Image(filename=imgs[0], key = "_img_")],
          [sg.Text("The live long gesture is used to pause or play a video.", key = "_text3_", visible=True)],
          [sg.Text("Click the 'Next' button to view the next gesture", key = "_text4_", visible=True)], 
          [sg.Button("Next", key="Next",visible=True)],
          [sg.Button("Back", key="Back",visible = True)]]
    return sg.Window("Gesture Control Tutorial", layout, element_justification='c', size=(750,700))

def createwindow2():
    layoutHome = [[sg.Text("Welcome to Gesture Control", font=(500))],
                [sg.Image(filename=imgs[7])],
                [sg.Text("", size=(2,2))],
                [sg.Text("Click to view gesture options")], [sg.Button("Tutorial")],
                [sg.Text("Click to launch Gesture Control")], [sg.Button("Start"),sg.Checkbox("Display visuals", default = True, key = "_display_")],
                [sg.Text("Click to close Gesture Control")], [sg.Button("Stop")],
                [sg.Text("", size=(8,8))],
                [sg.Text("Developed for CISC/CMPE 325 by:")],
                [sg.Text("Trevor Kirton, Randy Bornstein, Jordan Belinksy, Andrew Lacey, and JJ Schroeder")]]
    return sg.Window("Gesture Control Home", layoutHome, element_justification='c', size=(750,700))

Tutorial = True
Back = False
windowHome = createwindow2()
while True:
    event, values = windowHome.read()

    if event == "Tutorial":
        #windowHome.close()
        windowTutorial = createwindow()
        tutPage = 0
        while Tutorial:
            event, values = windowTutorial.read()
            if event == "Next":
                Back = False
                tutPage+=1
            elif event == "Back":
                Back = True
                tutPage-=1
            elif event == "Close" or event == sg.WIN_CLOSED:
                windowTutorial.close()
                Tutorial = False
                #windowHome.close()
                #quit()
            if Tutorial:
                print(tutPage)
                if tutPage == 8 or tutPage == -1:
                    windowTutorial["Next"].update("Next")
                    windowTutorial.close()
                    Tutorial = False
                elif tutPage == 1:
                    windowTutorial["_text3_"].update(visible = False)
                    #windowTutorial["_text4_"].update(visible = False)
                    #windowTutorial["_text2_"].update(text2s[1])
                    windowTutorial["_text2_"].update(visible = False)
                elif tutPage == 0:
                    windowTutorial["_text2_"].update(visible = True)
                    windowTutorial["_text3_"].update(visible = True)
                    windowTutorial["_text4_"].update(visible = True)
                elif tutPage == 7:
                    windowTutorial["Next"].update("Start")
                    windowTutorial["_text2_"].update(text2s[2], visible=True)
                    windowTutorial["_img_"].update(imgs[7])
                    windowTutorial["_text4_"].update(visible = False)
                elif tutPage == 6 and Back == True:
                    windowTutorial["Next"].update("Next")
                    windowTutorial["_text2_"].update(text2s[0])
                    windowTutorial["_img_"].update(visible=True)
                if -1<tutPage<7:
                    windowTutorial["_img_"].update(imgs[tutPage])
                if -1<tutPage <= 7:
                    windowTutorial["_head_"].update(heads[tutPage])
                    windowTutorial["_text1_"].update(text1s[tutPage])
        Tutorial = True
        #event, values = windowHome.read()
    elif event == "Start" and gestureControl.running == False:
        print(values["_display_"])
        gestureControl.visual = values["_display_"]
        gestureControl.running = True
        thread = threading.Thread(target = gestureControl.run)
        thread.start()

        #event, values = windowLaunch.read()
        # if event == "Close" or event==sg.WIN_CLOSED:
        #     windowLaunch.close()
        #     quit()

    elif event == "Stop" and gestureControl.running == True:
        gestureControl.running = False
        thread.join()

    elif event == sg.WIN_CLOSED:
        if gestureControl.running == True:
            thread.join()
        windowHome.close()
        quit()
