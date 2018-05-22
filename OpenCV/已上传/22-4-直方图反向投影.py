'''
直方图反向投影可以用来做图像分割，或者在图像中寻找我们感兴趣的部分。
也就是说，它会输出与输入图像同样大小的图像，其中的每一个像素值代表输入图像上对应点属于目标图像的概率。
如何实现这个算法呢？

1、原理
    首先我们要为包含目标的图像创建直方图。
    我们要查找的对象要尽量占满这张图像。最好使用颜色直方图。
    然后我们把这个颜色直方图投影到输入图像中寻找我们的目标，
    也就是找到输入图像中的每一个像素点的像素值在直方图对应的概率。
    这样就得到一张概率图像，最后设置适当的阈值对概率图象进行二值化。

'''

'''
2、Numpy中的算法
    首先要创建两幅颜色直方图，目标图像的直方图M，输入图像的直方图I。
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

roi=cv2.imread('pic/messi_grass.jpg')
hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

target=cv2.imread('pic/messi.jpg')
hsvt=cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# M=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
# I=cv2.calcHist([hsvt],[0,1],None,[180,256],[0,180,0,256])
'''
    然后计算比值R=M/I。
    反向投影R就是根据R这个调色板创建一副新的图像，其中的每一个像素代表这个点就是目标的概率。
    请看代码：
'''
# R=M/I
# h,s,v=cv2.split(hsvt)
# B=R[h.ravel(),s.ravel()]
# B=np.minimum(B,1)
# B=B.reshape(hsvt.shape[:2])
#
# disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# B=cv2.filter2D(B,-1,disc)
# B=np.uint8(B)
# cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)
#
# ret,thresh=cv2.threshold(B,50,255,0)
#
# cv2.imwrite('pic/22-4-1.jpg',thresh)
# cv2.imshow('result',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #此处插入图像，22-4-1

'''
3、OpenCV中的反向投影
    提供函数calcBackProject()用来做直方图反向投影。
    
'''
roihist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst=cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
dst=cv2.filter2D(dst,-1,disc)

ret,thresh=cv2.threshold(dst,50,255,0)
thresh=cv2.merge((thresh,thresh,thresh))

res=cv2.bitwise_and(target,thresh)
res=np.hstack((target,thresh,res))
cv2.imwrite('pic/22-4-2.jpg',res)

cv2.imshow('1',res)
cv2.waitKey(0)
cv2.destroyAllWindows()