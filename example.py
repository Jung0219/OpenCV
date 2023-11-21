import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# kernels
smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
LargeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")


# convolution!

kernel = (1/9) * np.ones((3, 3), dtype="float32")
image = cv.imread("sample.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

iH, iW = image.shape[:2]
kH, kW = kernel.shape[:2]

padding = (kW - 1) // 2
image = cv.copyMakeBorder(image, padding, padding,
                          padding, padding, cv.BORDER_REPLICATE)
result = np.zeros((iH, iW), dtype="float32")

for y in np.arange(padding, iH + padding):
    for x in np.arange(padding, iW + padding):
        roi = image[y - padding: y + padding + 1, x - padding: x + padding + 1]
        k = (roi * kernel).sum()

        result[y - padding, x - padding] = k

result = (result * 255).astype("uint8")

plt.imshow(result)
plt.waitforbuttonpress()
plt.close("all")
