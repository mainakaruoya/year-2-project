import serial
from datetime import datetime as dt
from picamera import PiCamera
from signal import pause
from time import sleep

#this creates the camera object
camera = PiCamera()
camera.rotation = 180

#the port from which the serial input comes from, as well as the baudrate
serialTrigger = serial.Serial("/dev/ttyACM0" , 9600)

#the function that reads the serial input, called by the trigger function
def readSerialInput():
    serialTrigger.flushInput()
    readSerialTrigger = serialTrigger.readline()
    print(readSerialTrigger)
    return True

#this function captures still images
def cameraCapture():
    camera.start_preview(alpha=150)
    sleep(2)
    x = dt.now().strftime("%Y%m%d_%H%M%S")
    camera.capture('/home/pi/Desktop/Projects/image%s.jpg' % x)
    camera.stop_preview()
    print("Camera capture successful.")

#this function allows the user to read the contents of the log file
def viewLogFile():
    logfile = open("securitylog.txt", mode = 'r', encoding = 'utf-8')
    for line in logfile:
        print(line, end = '')

#this function updates the security log file
def updateLogFile():
    with open("securitylog.txt",'a',encoding = 'utf-8') as logfile:
        logfile.write("Motion detected at " + dt.now().strftime("%m-%d-%Y, %H:%M") + "\n")

#this function calls the fuction capturing images or recording videos;
#calls the serial reading function and uses the user´s input to determine the mode
def triggerFunction():
    print("Reading serial input..")
    if (readSerialInput() == True): 
        if (userInput == 1):
            cameraCapture()
            updateLogFile()
        elif(userInput == 2):
            videoCapture()
            updateLogFile()
        else:
            print("Error! Try again.")

#this function captures video
def videoCapture():
    print("Video here!")
    y = dt.now().strftime("%Y%m%d_%H%M%S")
    camera.start_preview(alpha=150)
    camera.start_recording('/home/pi/Desktop/Projects/video%s.h264' % y)
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()
    print("Video Capture Successful.")
    updateLogFile()

#sort of like the ´main´ function
while True:
    print("---")
    print("---Motion Activated Security Camera System---")
    print("Here are the options:")
    print("1. Activate system in camera mode.")
    print("2. Activate system in video mode.")
    print("3. View security log file.")
    print("4. Quit")
    userInput = int(input("Choose the mode you want: "))

    if (userInput == 1):
        triggerFunction()
    elif(userInput == 2):
        triggerFunction()
    elif(userInput == 3):
        viewLogFile()
    elif(userInput == 4):
        quit()
    else:
        print("Error!")
        
#asynchronous serial transmission
pause()
