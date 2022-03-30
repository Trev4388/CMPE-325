import PySimpleGUI as sg

sg.theme("DarkBlue")

layoutHome = [[sg.Text("Click to view gesture options")], [sg.Button("Tutorial")],
             [sg.Text("Click to launch Gesture Control")], [sg.Button("Start")],
             [sg.Text("Click to close Gesture Control")], [sg.Button("Close")]]


layoutTutorial1 = [[sg.Text("Welcome to the tutorial")],
                  [sg.Text("The purpose of the tutorial is to demonstrate how to perform each recognized gesture and explain what each gesture does.")],
                  [sg.Text("The first recognized gesture is called 'live long' and can be seen below:")],
                  [sg.Image(filename="live_long(pauseplay).png")],
                  [sg.Text("The live long gesture is used to pause or play a video.")],
                  [sg.Text("Click the 'Next' button to view the next gesture")], [sg.Button("Next")]]
layoutTutorial2 = [[sg.Text("The next recognized gesture is called 'fist' and can be seen below:")],
                  [sg.Image(filename="fist(DecreaseVolume).png")],
                  [sg.Text("The fist gesture is used to decrease the volume.")],
                  [sg.Text("Click the 'Next' button to view the next gesture")], [sg.Button("Next")]]
layoutTutorial3 = [[sg.Text("The next recognized gesture is called 'rock' and can be seen below:")],
                  [sg.Image(filename="rock(IncreaseVolume).png")],
                  [sg.Text("The rock gesture is used to increase the volume.")],
                  [sg.Text("Click the 'Next' button to view the next gesture")], [sg.Button("Next")]]
layoutTutorial4 = [[sg.Text("The next recognized gesture is called 'peace' and can be seen below:")],
                  [sg.Image(filename="peace(skipBack).png")],
                  [sg.Text("The peace gesture is used to skip backwards in a video.")],
                  [sg.Text("Click the 'Next' button to view the next gesture")], [sg.Button("Next")]]
layoutTutorial5 = [[sg.Text("The next recognized gesture is called 'okay' and can be seen below:")],
                  [sg.Image(filename="okay(skipForwards).png")],
                  [sg.Text("The okay gesture is used to skip forwards in a video.")],
                  [sg.Text("Click the 'Next' button to view the next gesture")], [sg.Button("Next")]]
layoutTutorial6 = [[sg.Text("The next recognized gesture is called 'thumbs down' and can be seen below:")],
                  [sg.Image(filename="thumbsDown(DecSpeed).png")],
                  [sg.Text("The thumbs down gesture is used to decrease playback speed in a video.")],
                  [sg.Text("Click the 'Next' button to view the next gesture")], [sg.Button("Next")]]
layoutTutorial7 = [[sg.Text("The next recognized gesture is called 'thumbs up' and can be seen below:")],
                  [sg.Image(filename="thumbsUp(IncSpeed).png")],
                  [sg.Text("The thumbs up gesture is used to increase playback speed in a video.")],
                  [sg.Text("Click the 'Next' button to view the final instructions")], [sg.Button("Next")]]
layoutTutorial8 = [[sg.Text("You have now learned all of the recognized gestures.")],
                  [sg.Text("You can now launch the gesture recognition system by clicking the 'Start' button below.")],
                  [sg.Text("Please make sure you have selected the tab in which the video is playing before attemting gestures.")],
                  [sg.Button("Start")]]

layoutLaunch = [[sg.Text("Welcome to the launch")],
                [sg.Text("Click to close")], [sg.Button("Close")]]

# Create the window
windowHome = sg.Window("Gesture Control Home", layoutHome, element_justification='c', size=(750,700))

windowTutorial1 = sg.Window("Gesture Control Tutorial", layoutTutorial1, element_justification='c', size=(750,700))
windowTutorial2 = sg.Window("Gesture Control Tutorial", layoutTutorial2, element_justification='c', size=(750,700))
windowTutorial3 = sg.Window("Gesture Control Tutorial", layoutTutorial3, element_justification='c', size=(750,700))
windowTutorial4 = sg.Window("Gesture Control Tutorial", layoutTutorial4, element_justification='c', size=(750,700))
windowTutorial5 = sg.Window("Gesture Control Tutorial", layoutTutorial5, element_justification='c', size=(750,700))
windowTutorial6 = sg.Window("Gesture Control Tutorial", layoutTutorial6, element_justification='c', size=(750,700))
windowTutorial7 = sg.Window("Gesture Control Tutorial", layoutTutorial7, element_justification='c', size=(750,700))
windowTutorial8 = sg.Window("Gesture Control Tutorial", layoutTutorial8, element_justification='c', size=(750,700))

windowLaunch = sg.Window("Gesture Control Launch", layoutLaunch, element_justification='c', size=(750,700))

# Create an event loop
while True:
    event, values = windowHome.read()

    if event == "Tutorial":
        windowHome.close()
        event, values = windowTutorial1.read()
        if event == "Next":
            windowTutorial1.close()
            event, values = windowTutorial2.read()
            if event == "Next":
                windowTutorial2.close()
                event, values = windowTutorial3.read()
                if event == "Next":
                    windowTutorial3.close()
                    event, values = windowTutorial4.read()
                    if event == "Next":
                        windowTutorial4.close()
                        event, values = windowTutorial5.read()
                        if event == "Next":
                            windowTutorial5.close()
                            event, values = windowTutorial6.read()
                            if event == "Next":
                                windowTutorial6.close()
                                event, values = windowTutorial7.read()
                                if event == "Next":
                                    windowTutorial7.close()
                                    event, values = windowTutorial8.read()
                                    if event == "Start":
                                        windowTutorial8.close()
                                        event, values = windowLaunch.read()
                                        if event == "Close" or event == sg.WIN_CLOSED:
                                            windowLaunch.close()
                                            quit()


    elif event == "Start":
        windowHome.close()
        event, values = windowLaunch.read()
        if event == "Close" or event==sg.WIN_CLOSED:
            windowLaunch.close()
            quit()

    elif event == "Close":
        windowHome.close();
        quit()
