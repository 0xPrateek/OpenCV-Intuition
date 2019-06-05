import cv2
# Loading cv2

image = cv2.imread('../test6.png')
# Loading image

image_mask = cv2.imread('../test6.png',0)
# Loading image in grayscale for masking.

inpainted_FMM = cv2.inpaint(img,img_mask,3,cv2.INPAINT_TELEA)
# image inpainting using Fast marching method

inpainted_NS = cv2.inpaint(img,img_mask,3,cv2.INPAINT_NS)
# image inpainting using Naiver stokes method

while True:

    # Displaying inpainted image
    cv2.imshow('FMM - inpainted ',inpainted_FMM)    
    cv2.imshow('NS - inpainged ',inpainted_NS)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
