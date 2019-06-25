
import numpy as np
import cv2

cap = cv2.VideoCapture('Video.flv')

# Getting the first frame of the video
ret,frame = cap.read()

# Setting location of the window
r,h,c,w = 250,90,400,125
track_window = (c,r,w,h)

# ROI for tracking
roi = frame[r:r+h, c:c+w]

# Converting to HSV format
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))

# Calculating Histogram of HSV image
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])

cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while True:
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # applying CamShift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Drawing on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True, 255,2)

        # Displaying image
        cv2.imshow('img2',img2)

        if cv2.waitKey(60) & 0xff == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)
    else:
        break

cv2.destroyAllWindows()
cap.release()
