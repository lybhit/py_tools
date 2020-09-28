#!/usr/bin/python

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = cv2.imread('1.jpg')
H_rows, W_cols= img.shape[:2]
print(H_rows, W_cols)
N = 30
X = 40
pts1 = np.float32([[77, 0], [171, 128], [77, 268], [0, 128]])
pts2 = np.float32([[126+N+X, 0],[252+N,128],[126+N+X, 268],[0,128]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (268+N,252+N))
cv2.imwrite("res.jpg",dst)
image_show_11 = Image.fromarray(img)
display(image_show_11)
image_show_12 = Image.fromarray(dst)
display(image_show_12)