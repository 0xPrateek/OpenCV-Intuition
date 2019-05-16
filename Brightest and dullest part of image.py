import cv2                     # Importing cv2
img = cv2.imread('image.jpeg')     # Loading image 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # converting img to gray since minMaxLoc() takes image in grayscale.

while True:
    gray = cv2.blur(gray,(5,5))      #Blurring image so that we can increase the robustness
    
    (minval,maxval,minloc,maxloc) = cv2.minMaxLoc(gray)   # The magical function which returns minimum & maximum pixel intensity as well as there location
    cv2.circle(img,maxloc,10,(255,0,0),3)      # Drawing circle over the image's brightest part
    cv2.circle(img,minloc,10,(0,255,0),3)      # Drawing circle over the image's darkest part
    cv2.imshow('Bright and Dark in Image',img)  #displaying image
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
