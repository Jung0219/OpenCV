"""
restarting the tutorial from the website
opencv stores image in the form of "Mat" object


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
