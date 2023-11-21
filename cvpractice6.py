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
    f. cv.bilateralFilter(image, )

5. image edges
    a. step edge
        i. abrupt change in pixel intensity
    b. ramp edge
        i. gradual change 
    c. ridge edge
        i. two ramp edges combined, up and down
        ii. roof edge: descend right away after reaching the highest point

6. canny edge detection
    a. gaussian smoothing
    b. gradient magnitude and orientation calculation
    c. non maxima suppression (selecting one highest-pixel value for the edge)
        i. based on gradient orientation (compare with other pixel values along the orientation)
    d. hysteresis thresholding
        i. T upper and lower, where lower and upper values are considered edge and non-edge values
        ii. if the region is connected through the upper value, see it as an edge
    e. cv.Canny(img, lowerThreshold, upperThreshold)     


Last left off with canny edge detection
Goal for next week: finish up with the contour detection program
make it into a solid github project
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kernelSizes = [(111, 111), (311, 311), (411, 411)]

image = cv.imread("sample.jpg")
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cannied = cv.Canny(imageRGB, 30, 150)

blurred = cv.GaussianBlur(imageRGB, (11, 11), 0)
blurredCanny = cv.Canny(blurred, 30, 150)

upperThresh, _ = cv.threshold(imageGray, 0, 255, cv.THRESH_OTSU)
lowerThresh = upperThresh / 2

canny3 = cv.Canny(blurred, lowerThresh, upperThresh)


plt.figure(figsize=(20, 15))
plt.subplot(141)
plt.imshow(cannied, cmap="gray")
plt.subplot(142)
plt.imshow(blurredCanny, cmap="gray")
plt.subplot(143)
plt.imshow(canny3, cmap="gray")
plt.waitforbuttonpress()
plt.close("all")
