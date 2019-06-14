'''
   Program Name :- 2D histogram plotting using openCV and Python
   Author Name :- Prateek Mishra (0xPrateek)
'''
# Importing modules
import cv2
import matplotlib.pyplot as plt

# Loading Image as grayscale
image = cv2.imread('test1.jpg')

# Converting BGR Image to HSV form of Image.
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# Calculating histogram
histogram = cv2.calcHist([hsv_image],[0,1],None,[180,256],[0,180,0,256])

# Ploting histogram
plt.plot(histogram,color="black")
plt.title("Grayscale Image histogram")
plt.xlabel("Pixel Values")
plt.ylabel("Pixel frequency")
plt.imshow(histogram,interpolation = 'nearest')
plt.show()
