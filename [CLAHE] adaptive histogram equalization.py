'''
   Program Name : Contrast Limited adaptive histogram Equilization
                                    or
                        Adaptive histogram Equilization
   Author Name : Prateek Mishra (0xPrateek)
'''

# Importing modules
import numpy as np
import cv2

# Loading image in Grayscale
image = cv2.imread('test0.jpg',0)

'''
 Creating a CLAHE object
 The arguments are optional.
 clipLimit : Is for limit for Contrast limiting
 tileGridSize : Is the number of blocks image will be divided in.
'''
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# Applying adaptive histogram Equilization
adaptive_image = clahe.apply(img)

while  True:

    # Displaying Adaptive Histogram Equilization Image
    cv2.imshow('Image',cl1)
    if cv2.waitKey(1)  & 0xFF == 27:
        break

cv2.destroyAllWindows()
