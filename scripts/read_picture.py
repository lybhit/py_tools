import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("../data/map_rtk_5.pgm" ,  cv2.IMREAD_GRAYSCALE)
print("pic shape, return (row number, col number, chanel number):", img.shape)
print("pixel number:", img.size)
print("pic type:", img.dtype)
#img = cv2.resize(img,(280,280))

fname = open("../data/pixel.txt",'w')
fname.write("pic shape, return (row number, col number, chanel number):"+str(img.shape) + '\n') #----1
fname.write("pixel number"+str(img.size)+'\n') #----2
fname.write("pic type"+str(img.dtype)+'\n') #----3
Xlenth = img.shape[1]#col number
Ylenth = img.shape[0]#row number
a = 1 #----4
for i in range(Ylenth):
    fname.write(str(a) + ':'+ '\n')#----5
    for j in range(Xlenth):
        fname.write(str(img[i][j]) + ' ' )
    a += 1#----6
fname.write('\n')
fname.close()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()