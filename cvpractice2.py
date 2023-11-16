"""
1. pixel manipulation
    a. individual pixel values can be changed
2. cropping
    a. give the image a certain frame to which it should be cropped
    b. pixel slicing, basically
    c. cv2.resize(img, dsize)
        i. for dsize, you can specify the pixel dimensions
        ii. or use scale factors fx = 2, fy = 2 (2 times larger), fx = 0.5, fy = 0.5 (0.5 times larger)
            1. in this case, use None for the dsize parameter merely resizing the pixels
3. flipping
    a. cv2.flip(img, flipcode)
        i. 0 = x axis
        ii. < 0 = y axis
        iii. > 0 = both axes
4. rotation
    a. cv2.getRotationMatrix2D(center, angle, scale)
"""

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile

# address = r"C:\Users\OWNER\Downloads\python\OpenCV\checkerboard_18x18.png"
imgBGR = cv2.imread("sample.jpg")
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# print(imgRGB.shape)
plt.figure(figsize=[30, 5])
plt.subplot(141)
plt.imshow(imgRGB)
plt.title("original")
plt.subplot(142)
plt.imshow(cv2.flip(imgRGB, 0))
plt.title("vertical flip")
plt.subplot(143)
plt.imshow(cv2.flip(imgRGB, 1))
plt.title("horizontal flip")
plt.subplot(144)
plt.imshow(cv2.flip(imgRGB, -1))
plt.title("both flip")

plt.waitforbuttonpress()
plt.close('all')
