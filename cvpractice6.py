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
        the computed value        

3. blurring (aka smoothing)
    a. thresholding and edge detection better when image smoothened (less noise and details)
    a. we must apply a filter to the image
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

address = "sample.jpg"
img = cv.imread(address)

yellow = np.uint8([[[255, 255, 0]]])
hsvYellow = cv.cvtColor(yellow, cv.COLOR_RGB2HSV)

lowerLimit = hsvYellow[0][0][0] - 10, 100, 100
upperLimit = hsvYellow[0][0][0] + 10, 255, 255

print(lowerLimit, upperLimit)
