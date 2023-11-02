"""
1. drawing a line
    a. cv2.line(img, pt1, pt2, color, thickness=thickness, lineType=lineType, )
        i. points are tuple values of pixel coordinates
        ii. color argument is (255, 255, 255)   
2. drawing a circle
    a. cv2.circle(img, center, radius, color, thickness=thickness, lineType=lineType)
3. drawing a rectangle
    a. cv2.rectangle(img, topLeft, bottomRight, color, thickness=thickness, lineType=lineType)
        i. negative thickness fills out the rectangle with color
4. putting text
    a. cv2.putText(img, text, org, fontFace, fontScale, color, thickness=thickness, lineType=lineType)
        i. org is the bottom left cornor of the textbox
        ii. fontFace is font type
        iii. fontScale is font size
"""

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sample.jpg")

text = "leafy"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

cv2.rectangle(img, (1000, 500), (2000, 1000), (255, 255, 255), -20)

plt.imshow(img[:,:,::-1])
plt.waitforbuttonpress()
plt.close('all')


