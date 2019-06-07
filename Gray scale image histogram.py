# Importing modules
import cv2
import matplotlib.pyplot as plt

# Loading Image as grayscale
image = cv2.imread('test1.jpg',0)

# Calculating histogram
histogram = cv2.calcHist([image],[0],None,[256],[0,256])

# Ploting histogram
plt.plot(histogram,color="black")
plt.title("Grayscale Image histogram")
plt.xlabel("Pixel Values")
plt.ylabel("Pixel frequency")
plt.show()
