# Loading modules
import cv2
import numpy as np

# Loading image
image = cv2.imread('test4.jpeg')

# Creating Kernel or Matrix which will be used for masking.
kernel = np.array([[0,0,-1],
                   [-1,2,4],
                   [1,2,-2]],np.float32)

# Using filter2D() for masking over every pixel of the image.
masked_image = cv2.filter2D(image,-1,kernel)

while True:
    # Displaying image
    cv2.imshow('Masked ',masked_image)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
