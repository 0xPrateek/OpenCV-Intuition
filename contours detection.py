import cv2  

img = cv2.imread('contour.png')    # Loading img
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     # converting it to grayscale(as required for canny(). )
edged_img = cv2.Canny(img,127,225)         # Detecting edges in the image
cnt,heirarchy = cv2.findContours(edged_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)     # Finding contours detection 
cv2.drawContours(img,cnt,-1,(255,0,0),2)        # Drawing the detected contours on the image.

while True:
    cv2.imshow('Contours',img)                 # Displaying image with detected contours.
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
