import cv2
import numpy as np

#  Loading image
img = cv2.imread('image/coins.jpg', cv2.IMREAD_COLOR)

# Converting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying hough transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=300 , minRadius=130, maxRadius=300)
# Acurracy can be obtained by changing minDist, minRadius,maxRadius parameter values.

# Drawing the detected circles
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw inner circle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

# Displaying image with circle
while True:
    cv2.imshow("Coins ", img)
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
