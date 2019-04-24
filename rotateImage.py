import cv2

img = cv2.imread('/images/SampleImage.jpg',0)
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

while True:
  # rotate the image by 180 degrees
  M = cv2.getRotationMatrix2D(center, 180, 1.0)
  rotated = cv2.warpAffine(image, M, (w, h))
  cv2.imshow("rotated", rotated)
  
  if(cv2.waitkey(0) & 0xFF == 27):
    break
cv2.destroyAllWindows()
