import cv2                            # Loading modules 
import numpy as np

im = cv2.imread("test6.jpg")          # Loading images for seamless cloning.
obj = cv2.imread("test3.png")

mask = 255 * np.ones(obj.shape, obj.dtype)    # Creating mask for Object image.
width, height, channels = im.shape            # Getting center of the main image.
center = (int(height / 2)-60, int(width / 2)+10)     # The (-60 & +10) here is just used for making the object at center.
output_mixed = cv2.seamlessClone(obj, im, mask,center , cv2.MIXED_CLONE)      # Seamless cloning by preserving background texture.
output_normal = cv2.seamlessClone(obj, im, mask,center , cv2.NORMAL_CLONE)    # Seamless cloning without preservation of texture

while True:
    cv2.imshow('Normal Seamless clone ',output_normal)      # Displaying image.
    cv2.imshow('Mixed Seamless clone ',output_mixed)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
