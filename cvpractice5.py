"""
Contour Detection program: following the tutorial from google
reading and drawing contours
1. reading
    a. cv2.findContours(image, contour retrieval mode, contour approximation method)
        i. retrieval modes:
            1. RETR_EXTERNAL: outer extreme
            2. RETR_LIST: all without hierarchy
            3. RETR_CCOMP: all in two-level hierarchy
            4. RETR_TREE: all in full hierarchy
            5. RETR_FLOODFILL: ?
        ii. approximation methods:
            1. CHAIN_APPROX_NONE: all contour points
            2. CHAIN_APPROX_SIMPLE: compress and leave end points
            3. CHAIN_APPROX_TC89_L1: tech-chin chain alg. 
            4. CHAIN_APPROX_TC89_KCOS: tech-chin chain alg.
2. drawing
    a. after extracting contour points and hierarcy using the findContour function
    b. cv2.drawContours(img, contours, index of contours (hierarchy), color, thickness, etc)
        i. for the index, use -1 to include all contours, or to draw the 3rd one, put 2 (0-indexed)

Steps for drawing contours:
    1. read the image
    2. turn the image into b/w
    3. threshold the image
    4. extract contour and hierarchy 
    5. draw contour
"""

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# read sample image
img = cv2.imread("sample.jpg")
# convert image to gray
sample = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# threshold the gray image
retval, thresholded = cv2.threshold(sample, 100, 255, cv2.THRESH_OTSU)
# get contour list
contours, hierarchy = cv2.findContours(
    thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# draw contour on images
cv2.drawContours(sample, contours, -1, (0, 0, 0), 1)
cv2.drawContours(img, contours, -1, (0, 0, 0), 1)
retval, result = cv2.threshold(sample, 254, 255, cv2.THRESH_BINARY)


cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)
cv2.imshow("thresh", img)

if cv2.waitKey(0):
    cv2.destroyAllWindows()


"""plt.imshow(sample)
plt.waitforbuttonpress()
plt.close('all')"""
