import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# Show image using opencv
cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()

# Show image using matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80,100], 'c', linewidth=5)
plt.show()

# Write image using opencv
cv2.imwrite('grayimg.png', img)
