"""
idea: given an image and a color, return the contour of the image drawn with the given color on black background
desktop application would be nice, but I'll just make it in the form of python function
"""
import matplotlib.pyplot as plt
import cv2 as cv

# read the image and convert it into black and white
address = ("sample3.jpg")


def contour(address, color=(255, 255, 255), thickness=1):
    img = cv.imread(address)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # threshold the image
    # use otsu's method to find the threshold value
    retval, thresh = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
    # find the contour
    contours, hierarchy = cv.findContours(
        thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # draw the contour on a black background
    retval, background = cv.threshold(img, 255, 255, cv.THRESH_BINARY)
    result = cv.drawContours(background, contours, -1, color, thickness)
    cv.imwrite("edge1.jpg", result)


def edge(address):
    img = cv.imread(address)
    edges = cv.Canny(img, 100, 200)
    cv.imwrite("edge.jpg", edges)


contour(address)
edge(address)

# experimenting whether I can make a contour with adaptively thresholded image
"""
img = cv.imread(address)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# threshold the image
# use otsu's method to find the threshold value
thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 45, 0)
# find the contour
contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# draw the contour on a black background
retval, background = cv.threshold(img, 255, 255, cv.THRESH_BINARY)
result = cv.drawContours(background, contours, -1, (0, 0, 0), 10)

plt.figure(figsize=(10, 10))
plt.imshow(result, cmap="gray")
plt.waitforbuttonpress()
plt.close("all")
"""

"""
img = cv.imread(address)
edges = cv.Canny(img, 100, 200)

plt.figure(figsize=(10, 10))
plt.imshow(edges, cmap="gray")
plt.waitforbuttonpress()
plt.close("all")
"""
