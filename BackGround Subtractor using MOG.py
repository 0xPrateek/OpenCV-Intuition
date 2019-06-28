'''
    Program name : BackGround Subtraction using MOG in python
    Author name : Prateek Mishra    
'''

# Import modules
import numpy as np
import cv2

# Creating video Caputure object
cap = cv2.VideoCapture('InputVideo.avi')

# Creating BackGround subtactor object
subtactor = cv2.createBackgroundSubtractorMOG()

while True:

    # Reading Frames from video
    ret, frame = cap.read()

    # Applying MOG BackGround subtactor
    fgmask = subtactor.apply(frame)

    # Displaying output Frame
    cv2.imshow('frame',fgmask)
    if cv2.waitKey(30) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
