import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def imgThreshold(inputImg, fileName):
    img = cv2.imread(inputImg, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    blocksize = max(h, w) // 100
    if blocksize % 2 == 0:
        blocksize -= 1
    thresholded = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, -5)
    cv2.imwrite(fileName, thresholded)


#threshold("sample5.jpg")
"""
images = ["sample1.jpg", "sample2.jpg", "sample3.jpg", "sample4.jpg", "sample5.jpg"]
original = cv2.imread(images[1])
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY) # gray image
"""
imgThreshold("pattern.jpg", r"c:/Users/OWNER/Downloads/python/OpenCV/saved45.jpg")


"""
adaptiveThresholded1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 539, 3)
adaptiveThresholded2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 5)
adaptiveThresholded3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)

retval, thresholded1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
retval, thresholded2 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
retval, thresholded3 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

plt.figure(figsize=[15, 10])

plt.subplot(231);plt.imshow(adaptiveThresholded1, cmap="gray")
plt.subplot(232);plt.imshow(adaptiveThresholded2, cmap="gray")
plt.subplot(233);plt.imshow(adaptiveThresholded3, cmap="gray")
plt.subplot(234);plt.imshow(thresholded1, cmap="gray")
plt.subplot(235);plt.imshow(thresholded2, cmap="gray")
plt.subplot(236);plt.imshow(thresholded3, cmap="gray")

#plt.subplot(224);plt.imshow(original)

plt.waitforbuttonpress()
plt.close('all')
"""