# Importing modules
import cv2
import matplotlib.pyplot as plt

# Importing image
image = cv2.imread('test1.jpg')

# Defining the BGR colors
colors = ('b','g','r')

# Calculating and Ploting histogram of BGR color individually
for index,color in enumerate(colors):
    histogram = cv2.calcHist([image],[index],None,[256],[0,256])
    plt.plot(histogram,color=color)

# Showing histogram plot
plt.title('Colored image histogram')
plt.xlabel('Pixel Values')
plt.ylabel('Pixel Frequency')
plt.show()
