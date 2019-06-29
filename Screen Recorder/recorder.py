'''
Program - SCREEN RECORDER USING PYTHON OPENCV
Author - Prateek Mishra
'''

import numpy as np
import pyautogui
import imutils
import cv2

codec=cv2.VideoWriter_fourcc(*'MJPG')            #Type of Video ,in this case AVI
output_name='NewVideo.avi'                       #Name of saved video file.
fps=25                                           #Frames per second of video
dimension=(640,480)                              #Height and Width of video

#object for writing Video on disk
writevideo =cv2.VideoWriter(output_name,codec,fps,dimension)

count=1
while True:

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    writevideo.write(image)
    print(" Saved : ",count)
    cv2.imshow("Image",image)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
    count+=1

#Finally free up the objects.
cap.release()
cv2.destroyAllWindows()
