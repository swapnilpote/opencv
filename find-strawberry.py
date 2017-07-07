from __future__ import division
import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin

def find_strawberry(image):
	# rgb red green blue
	# bgr blue green red
	# step-1 : convert to the correct color scheme
	image = cv2.cvtColor(image, COLOR_BGR2RGB)

	# step-2 : scale our image properly
	max_dimension = max(image.shape)
	scale = 700/max_dimension
	image = cv2.resize(image, None, fx=scale, fy=scale)

	# step-3 : clean our image
	image_blur = cv2.GaussianBlur(image, (7, 7), 0)
	image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)

	# step-4 : define filters
	min_red = np.array([0, 100, 80])
	max_red = np.array([10, 256, 256])

	mask1 = cv2.inRange(image_blur_hsv, min_red, max_red)

	# filter by brightness
	min_red2 = np.array([170, 100, 80])
	max_red2 = np.array([180, 256, 256])

	mask2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)

	# take those 2 mask and combine them
	mask = mask1 + mask2

	# step-5 : segmentation