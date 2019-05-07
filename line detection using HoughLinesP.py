import cv2
import numpy as np

# loading image
img = cv2.imread('road.jpg', cv2.IMREAD_COLOR)

# Convert img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting edges in the image 
edges = cv2.Canny(gray, 1000, 500)       # Changing threshold values also helps in increasing accuracy.

# Detect points forming line
lines = cv2.HoughLinesP(edges, 20, np.pi/180,0, minLineLength=1, maxLineGap=5)   # Choose parameter values depending upon image

# Drawing lines on img
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

# Displaying the magic we just did...!
while True:
    cv2.imshow("lines in image ",img)
    if cv2.waitKey(0) & 0xFF ==27:
        break
cv2.destroyAllWindows()
