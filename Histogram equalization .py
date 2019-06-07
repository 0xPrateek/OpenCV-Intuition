# Loading modules
import cv2

# Loading image
image = cv2.imread('test4.jpeg',0)

# Equilizing histogram of the image
equilize = cv2.equalizeHist(image)
import matplotlib.pyplot as plt
while True:

    # Displaying image
    cv2.imshow('Equilized Image',equilize)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
