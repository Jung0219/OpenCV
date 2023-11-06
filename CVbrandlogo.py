import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


def brandLogoPattern(brandLogo, imgPattern, directory):
    # read images
    logo = cv2.imread(brandLogo)
    pattern = cv2.imread(imgPattern)
    # resize pattern to fit the logo
    logoSize = logo.shape
    pattern = cv2.resize(pattern, (logoSize[1], logoSize[0]))
    # read image in RGB
    """logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
    pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2RGB)"""
    # create b/w image of logo
    logoBW = cv2.cvtColor(logo, cv2.COLOR_RGB2GRAY)
    # create masks
    # ask for the logo color
    ans = input("is the logo closer to black or white? b, w\n")
    while ans != "b" and ans != "w":
        ans = input("is the logo closer to black or white? b, w\n")
    if ans == "b":
        retval, logoMask = cv2.threshold(
            logoBW, 100, 255, cv2.THRESH_BINARY_INV)
    else:
        retval, logoMask = cv2.threshold(logoBW, 100, 255, cv2.THRESH_BINARY)
    invLogoMask = cv2.bitwise_not(logoMask)
    # merge pattern into logo
    patternLetters = cv2.bitwise_and(pattern, pattern, mask=logoMask)
    foreground = cv2.bitwise_and(logo, logo, mask=invLogoMask)
    # result
    result = cv2.add(patternLetters, foreground)

    cv2.imwrite(directory, result)


brandLogoPattern("brands.png", "pattern.jpg",
                 r"c:/Users/OWNER/Downloads/python/OpenCV/saved45.jpg")


"""
img1 = cv2.imread("emart.png")
img2 = cv2.imread("pattern.jpg")
# get two images, emart logo and the pattern to be inserted
img1_shape = img1.shape
img2 = cv2.resize(img2, (img1_shape[1], img1_shape[0]))
emart = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
pattern = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# read the brand logo in black and white
emartGray = cv2.cvtColor(emart, cv2.COLOR_RGB2GRAY)
# threshold the b/w brand logo to make a mask (letters are white)
retval, imgMask = cv2.threshold(emartGray, 100, 255, cv2.THRESH_BINARY)
# create inverse mask (letters black)
invImgMask = cv2.bitwise_not(imgMask)
patternLetters = cv2.bitwise_and(pattern, pattern, mask=imgMask)
background = cv2.bitwise_and(emart, emart, mask=invImgMask)
print(patternLetters.shape)
print(background.shape)
# you can also use add. here
result = cv2.bitwise_or(patternLetters, background)

plt.figure(figsize=[15,5])

plt.subplot(131);plt.imshow(patternLetters, cmap="gray");plt.title(str(emart.shape))
plt.subplot(132);plt.imshow(background, cmap="gray");plt.title(str(pattern.shape))
plt.subplot(133);plt.imshow(result)
plt.waitforbuttonpress()
plt.close('all')
"""
