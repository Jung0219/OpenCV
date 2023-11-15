import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input file")
# ap.add_argument("-o", "--output", required=True, help="path to output file")
args = vars(ap.parse_args())
print(args)

image = cv.imread(args["input"])
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 0)
retval, thresh = cv.threshold(gray, 100, 255, cv.THRESH_OTSU)
