import os 
import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread("emart.png")
img2 = cv2.imread("pattern.jpg")

emart = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
pattern = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

emartGray = cv2.cvtColor(emart, cv2.COLOR_RGB2GRAY)
retval, emartBlack = cv2.threshold(emartGray, 100, 255, cv2.THRESH_BINARY_INV)
emartB = cv2.cvtColor(emartBlack, cv2.COLOR_GRAY2RGB)


patternLetters = cv2.bitwise_or(emartB, pattern)

foreground = cv2.bitwise_and(emart, emart, emartB)

plt.figure(figsize=[15,5])

plt.subplot(131);plt.imshow(emartB, cmap="gray");plt.title(str(emart.shape))
plt.subplot(132);plt.imshow(emartBlack, cmap="gray");plt.title(str(pattern.shape))
plt.subplot(133);plt.imshow(foreground)
plt.waitforbuttonpress()
plt.close('all')
