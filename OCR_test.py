from cv2 import cv2
import numpy as np


img = cv2.imread('IMG.jpg')

cv2.imshow('Result', img)
cv2.waitKey(0)

