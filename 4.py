import numpy as np
import cv2

img = cv2.imread('image.png', cv2.IMREAD_COLOR)

# Change value at 55,55 pixel
img[55,55] = [255,255,255]
px = img[55, 55]
print(px)

# Print value inside this region
roi = img[100:150, 100:150]
print(roi)

# Fill roi with white color
img[100:150, 100:150] = [255,255,255]


# Cut certain part of image
region_img = img[137:211, 207:294]
img[0:74, 0:87] = region_img

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
