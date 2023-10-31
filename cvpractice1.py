"""
1. cv2.imread(r"filepath") 
    a. read datas of the file



"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

address = r"C:\Users\OWNER\Pictures\Lightroom Saved Photos\Sangju 05_22_2023\Places\DSC07897.jpg"

img = cv2.imread(address)
print(cv2.split(img))

"""plt.figure(figsize=[10,5])

plt.subplot();plt.imshow(r, cmap="gray");plt.title("Red")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue")


imgMerged = cv2.merge((b,g,r))
plt.subplot(144);plt.imshow(imgMerged[:,:,::-1]);plt.title("Merged")
plt.waitforbuttonpress()"""