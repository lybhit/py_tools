import cv2
import numpy as np
from PIL import Image
 
R = 0.45
 
def drawMatchesKnn_cv2(img1_gray,kp1,img2_gray,kp2,Match):
    h1, w1 = img1_gray.shape[:2]
    h2, w2 = img2_gray.shape[:2]
    vis = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
    vis[:h1, :w1] = img1_gray
    vis[:h2, w1:w1 + w2] = img2_gray
    p1 = [kpp.queryIdx for kpp in Match]
    p2 = [kpp.trainIdx for kpp in Match]
    post1 = np.int32([kp1[pp].pt for pp in p1])
    post2 = np.int32([kp2[pp].pt for pp in p2]) + (w1, 0)
    for (x1, y1), (x2, y2) in zip(post1, post2):
        cv2.line(vis, (x1, y1), (x2, y2), (0,255,0),1)
    image_show_4 = Image.fromarray(vis)
    display(image_show_4)
 
def perspectiveTransformation(img1_gray, img2_gray):
#     image_show_1 = Image.fromarray(img1_gray)
#     display(image_show_1)
#     image_show_2 = Image.fromarray(img2_gray)
#     display(image_show_2)
    surf = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = surf.detectAndCompute(img1_gray, None)
    kp2, des2 = surf.detectAndCompute(img2_gray, None)
    bf = cv2.BFMatcher(cv2.NORM_L2)
    matches = bf.knnMatch(des1, des2, k = 2)
    Match = []
    for m,n in matches:
        if m.distance < R * n.distance:
            Match.append(m)
    if len(Match) > 4:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in Match ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in Match ]).reshape(-1,1,2)
        M,status  = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)        
    dst = cv2.warpPerspective(img1_gray, M, (img2_gray.shape[0]*2,img2_gray.shape[1]*2))
    drawMatchesKnn_cv2(img1_gray,kp1,img2_gray,kp2,Match[:15])
    image_show_3 = Image.fromarray(dst)
    display(image_show_3)
    return dst
 
img1_gray = cv2.imread("待变换.jpg")
img2_gray = cv2.imread("模板图.jpg")
pt = perspectiveTransformation(img1_gray, img2_gray)
raw = cv2.cvtColor(pt,cv2.COLOR_BGR2RGB)
raw_gray = cv2.cvtColor(raw,cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(raw_gray,125,350)
image1 = Image.fromarray(edges.astype('uint8')).convert('RGB')
display(image1)