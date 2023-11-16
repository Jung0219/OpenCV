import cv2 as cv
import numpy as np

# convolution!

kernel = (1/9) * np.ones((3, 3), dtype="float32")
image = cv.imread("sample.jpg")

iH, iW = image.shape[:2]
kH, kW = kernel.shape[:2]

padding = (kW - 1) // 2  # padding
# make a padding on the image
image = cv.copyMakeBorder(image, padding, padding,
                          padding, padding, cv.BORDER_REPLICATE)
result = np.zeros((iH, iW), dtype="float32")

for y in range(padding, iH + padding):
    for x in range(padding, iW + padding):
        roi = image[y - padding: y + padding + 1, x - padding: x + padding + 1]
        k = (roi * kernel).sum()

        result[y - padding, x - padding] = k

cv.imshow(result)
