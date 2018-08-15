#Importing cv2 for image reading and opening.
import cv2

#Using cv2.imread() function for reading the image file (Case sensitive). It takes two arguments :- file name and type of image[BGR(1),GrayScale(0),withoutAlpha(-1)]
img = cv2.imread("SampleImage.jpg",0)

while True:

#Using cv2.imshow() function for showing the image file. It also takes two arguments :- Title of the window and the object name in which we have read the image file.
    cv2.imshow("Sample Title ",img)

#Using cv2.waitkey() function for checking for the keypress events. This takes single argument , which is for time for which we have to wait .
    k= cv2.waitKey(1)
    if k & 0xFF == 27: 					#0xFF is written only if your device is 64-bit else you can ignore it. and 27 is for capturing for 'esc' key.

        break

#Using cv2.destroyAllwindows() for killing all the opened windows.
cv2.destroyAllWindows()