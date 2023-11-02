"""
controlling brightness
1. cv2.add(img, matrix) / cv2.subtract(img, matrix)
    i. control brightness by adding pixel values to every pixel
    ii. this is how you control the exposure, shadow, and hightlight in the image!!!!!!
2. cv2.multiply(img, matrix)
    i. control contrast by enhancing pixel values
    ii. the datatypes do not match; np adjustments needed
    iii. if val > 255, clipping needed (np)
3. cv2.threshold(src, thresh, maxval, type)
    i. returns 2 values: ret and nparray (image)
    ii. https://docs.opencv.org/3.4/db/d8e/tutorial_threshold.html for different types of thresholds
4. cv2.adaptiveThreshold(src, maxval, adaptiveMethod, type, blocksize, C)
    i. this returns only one value (image, np array)
    ii. two adaptive methods
        a. cv2.ADAPTIVE_THRESH_MEAN_C = taking means of the values around the pixel (block) - c
        b. cv.ADAPTIVE_THRESH_GAUSSIAN_C = taking gaussian sum - c
    iii. blocksize % 2 has to be 1
5. bitwise operations
    i. cv2.bitwise_and, cv2.bitwise_or, cv2.bitwise_xor, cv2.bitwise_not
    ii. putting two images together
        a. because black is 0, you convert certain parts of an image to black and put them together.
"""


import os 
import numpy as np
import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread("image.jpg")
img = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

adaptiveThresh1 = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 1001, -5)
adaptiveThresh2 = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, -10)
adaptiveThresh3 = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, -15)
adaptiveThresh4 = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, -20)
adaptiveThresh5 = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, -50)

lst = [adaptiveThresh1, adaptiveThresh2, adaptiveThresh3, adaptiveThresh4, adaptiveThresh5]

plt.figure(figsize=[20, 5])
for i in range(5):
    plt.subplot(1, 5, i + 1); plt.imshow(lst[i], cmap="gray")

plt.waitforbuttonpress()
plt.close('all')





"""
matrix = np.ones(img.shape, dtype="uint8") * 50
imgBrighter = cv2.add(img, matrix)
imgDarker = cv2.subtract(img, matrix)

plt.figure(figsize=[20,5])

plt.subplot(152);plt.imshow(imgBrighter)
plt.subplot(153);plt.imshow(img)
plt.subplot(154);plt.imshow(imgDarker)


plt.waitforbuttonpress()
plt.close('all')
"""

"""
matrix1 = np.ones(img.shape) * 1.5
matrix2 = np.ones(img.shape, dtype="uint8") * 50

highContrast = np.uint8(np.clip(cv2.multiply(np.float64(img), matrix1), 0, 255))
brighter = cv2.add(img, matrix2)

plt.figure(figsize=[20, 5])
plt.subplot(131);plt.imshow(highContrast)
plt.subplot(132);plt.imshow(img)
plt.subplot(133);plt.imshow(brighter)

plt.waitforbuttonpress()
plt.close('all')
"""

