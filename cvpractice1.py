"""
1. cv2.imread(r"filepath") 
    a. read datas of the file
2. cv2.split(image)
    a. splitting the image into images composed only of r, g, and b values
3. cv2.merge(r, g, b)
    a. opposite of split, takes in however many arguments
4. cv2.cvtColor(inputImage, conversionCode)
    a. convert colors from RGB to BRG, etc
        i. cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV, etc
    b. OpenCV retrieves images as BRG instead of RGB
    c. to merge, the three values must be in r, g, and b, not other format: another conversino required
5. cv2.imwrite(filename, img[parameters])
    a. storing newly composed images

"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

address = r"C:\Users\OWNER\Pictures\Lightroom Saved Photos\Sangju 05_22_2023\Places\DSC07897.jpg"

img = cv2.imread(address)
newImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(newImg)
plt.imshow(img)
plt.waitforbuttonpress()

plt.figure(figsize=[20,5])

plt.subplot(151);plt.imshow(h, cmap="gray");plt.title("hue")
plt.subplot(152);plt.imshow(s, cmap="gray");plt.title("saturation")
plt.subplot(153);plt.imshow(v, cmap="gray");plt.title("value")
plt.subplot(154);plt.imshow(img);plt.title("original image")
imgMerged = cv2.merge((h,s,v))
plt.subplot(155);plt.imshow(imgMerged);plt.title("Merged")
plt.waitforbuttonpress()