'''
    Program Name :- Background Subtraction using GMG
    Author Name :- Prateek Mishra
'''
# Importing modules
import numpy as np
import cv2

# Creating Video capture object for input Video
cap = cv2.VideoCapture('InputVideo.avi')

# Creating 3x3 kernel for using in morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

# Creating object for BackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorGMG()

while True:

    # Reading frame by frame from video
    ret, frame = cap.read()

    # Applying Background Subtraction to the frame
    fg_mask = fgbg.apply(frame)

    # Applying morphology on the masked foreground subtracted frame with an elipse kernel of 3x3
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

    # Displaying image
    cv2.imshow('GMG Subtractor',fg_mask)

    if cv2.waitKey(30) & 0xff == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
