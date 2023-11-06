"""
# my first goal is to make a program that returns the black and white contour of an image
1. cv2.imread(r"filepath") 
    a. read datas of the file
    b. second argument
        i. cv2.IMREAD_COLOR (1)
        ii. cv2.IMREAD_GRAYSCALE (0)
        iii. cv2.IMREAD_UNCHANGED (-1)
2. cv2.split(image)
    a. splitting the image into images composed only of r, g, and b values
        i. r, g, b = cv2.split(image)
3. cv2.merge(r, g, b)
    a. opposite of split, takes in however many arguments
4. cv2.cvtColor(inputImage, conversionCode)
    a. convert colors from RGB to BRG, etc
        i. cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV, etc
    b. OpenCV retrieves images as BRG instead of RGB
    c. to merge, the three values must be in r, g, and b, not other format: another conversino required
5. cv2.imwrite(filename, img[parameters])
    a. storing newly composed images
6. ndarray.shape 
    a. image is a numpy array(gets the width, height, and channels of the image)
    b. when extracting, leave unused values to _
        i. e.g., h, w, _ = im.shape
    c. or access it using index[0] for height, [1] for width, [2] for channels
    d. python slicing can be used here 
        i. e.g., im.shape[1::-1]


"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

address = r"C:\Users\OWNER\Pictures\Lightroom Saved Photos\Sangju 05_22_2023\Places\DSC07897.jpg"
"""
img = cv2.imread(address)
newImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(newImg)
plt.waitforbuttonpress()

plt.figure(figsize=[20,5])

plt.subplot(151);plt.imshow(h, cmap="gray");plt.title("hue")
plt.subplot(152);plt.imshow(s, cmap="gray");plt.title("saturation")
plt.subplot(153);plt.imshow(v, cmap="gray");plt.title("value")
plt.subplot(154);plt.imshow(img);plt.title("original image")
imgMerged = cv2.merge((h,s,v))
plt.subplot(155);plt.imshow(imgMerged);plt.title("Merged")
plt.waitforbuttonpress()
"""
newAddress = r"C:\Users\OWNER\Pictures\Lightroom Saved Photos\Sangju 05_22_2023\experiment"

img = cv2.imread(address)
b, g, r = cv2.split(img)
#reversing bgr to rgb
newImg = cv2.merge((r, g, b))
os.chdir(r"C:\Users\OWNER\Pictures\Lightroom Saved Photos\Sangju 05_22_2023\experiment")
cv2.imwrite("imwrite_image.jpg", newImg)

