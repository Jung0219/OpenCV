"""
restarting the tutorial from the website
opencv stores image in the form of "Mat" object
too many colors! 256 * 256 * 256
algorithm can't handle that many => color space reduction
round the value down (leave the last digit) by Inew = (Iold / 10) * 10
but since division & multiplication are expensive, we use hash table 

after the image thresholding tutorial, the opencv's website starts talking about the 
videos, which I'm not interested

I'm going to learn canny and blur on my own

1. canny
    a. cany edge detection algorithm made by a guy named Canny (duh)
    b. takes in up to 5 arguments
        i. cv.Canny(img, lowerBound, upperBound, aperture, gradient)
            1. not too sure what the last two are
        ii. but lower and upper bound works similar to image thresholding
        iii. the difference is that if the edge goes through the bound, as long as it is 
            above the upper bound, it will remain connected 

2. convolution
    a. kernel is basically a small matrix
        i. so a kernel size is a m x n matrix
        ii. it moves over an image an does mathematical operations
        iii. there has to be a middle value, so usually odd
    b. mathematical operation on the kernel region, then replace the same coordinate with
        the computed value with the neighboring pixels
    c. image gradients
        i. directional change in image intensity (areas that form a line with same intensity)
        ii. also uses kernel
        iii. change in x and change in y calculated
            1. Gx = I(x + 1, y) - I(x - 1, y)
            2. Gy = I(x, y + 1) - I(x, y - 1)
        iv. from here, we get gradient magnitude and gradient orientation 
        v. you basically draw a triangle
            1. gradient magnitude : magnitude of change in intensity
                a. gradient magnitude is sqrt(Gx ^ 2 + Gy ^ 2)
            2. gradient orientation : the diretion of the change in intensity
                a. arctan(Gy, Gx)
            3. then convert to degrees (180 / pi)
3. Sobel and Scharr kernels
    a. two kernels, one for horizontal change and one for vertical change
        i. horizontal (sobel and scharr)
            [-1, 0, 1], [3, 0, -3],
            [-2, 0, 2], [10, 0, -10],
            [-1, 0, 1], [3, 0, -3]
        ii. vertical:
            [-1, -2, -1], [3, 10, 3],
            [0, 0, 0],    [0, 0, 0]  
            [1, 2, 1]     [-3, -10, -3]  

4. blurring (aka smoothing)
    a. thresholding and edge detection better when image smoothened (less noise and details)
    b. bigger the kernel, blurrier the image
    c. cv.blur(image, kernel(x, y))
    d. cv.gaussianBlur(image, kernel(x, y)) (weighted blurring)
    e. cv.medianBlur(image, kernel(x, y)) (replace center pixel with median)
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kernelSizes = [(111, 111), (311, 311), (411, 411)]

image = cv.imread("sample.jpg")
imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

normalBlur = cv.blur(imageRGB, (111, 111))
gaussianBlur = cv.GaussianBlur(imageRGB, (111, 111), 0)
medianBlur = cv.medianBlur(imageRGB, 211)
bilateralBlur = cv.bilateralFilter(imageRGB, 111, 211, 71)

plt.figure(figsize=(15, 15))
plt.subplot(141)
plt.imshow(normalBlur)
plt.subplot(142)
plt.imshow(gaussianBlur)
plt.subplot(143)
plt.imshow(medianBlur)
plt.subplot(144)
plt.imshow(bilateralBlur)
plt.waitforbuttonpress()
plt.close("all")
