import cv2
import numpy as ns

cap = cv2.VideoCapture(0)

##  Details for Video ##

codec=cv2.VideoWriter_fourcc('D','I','V','X')    #Type of Video ,in this case AVI
output_name='NewVideo.avi'                       #Name of saved video file.
fps=25                                           #Frames per second of video
dimension=(640,480)                              #Height and Width of video

#object for writing Video on disk
writevideo =cv2.VideoWriter(output_name,codec,fps,dimension)

while(cap.isOpened()):

    ret,frame =cap.read()

    if ret is True:
        cv2.imshow('Video Title', frame)

        #This will write captured video on disk.
        writevideo.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#Finally free up the objects.
cap.release()
cv2.destroyAllWindows()
