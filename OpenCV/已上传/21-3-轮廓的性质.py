'''
有了轮廓之后， 我们经常需要提取一些对象特征。

1、长宽比
    边界矩形的宽高比：Width/Height
'''
import cv2 as cv
import numpy as np
x,y,w,h=cv.boundingRect(cnt)
aspect_ratio=float(w)/h

'''
2、Exent
    表示轮廓面积和边界矩形面积的比例。
    ObjectArea/BoundingRectangleArea
'''
area=cv.contourArea(cnt)
x,y,w,h=cv.boundingRect(cnt)
rect_area=w*h
extent=float(area)/rect_area

'''
3、Solidity
    轮廓面积和凸包面积的比。
    ContourArea/ConvexHullArea
'''
area=cv.contourArea(cnt)
hull=cv.convexHull(cnt)
hull_area=cv.contourArea(hull)
solidity=float(area)/hull_area

'''
4、Equivalent Diameter
    与轮廓面积相等的圆形的直径
'''
area=cv.contourArea(cnt)
equi_diameter=np.sqrt(4*area/np.pi)

'''
5、方向
    对象的方向，指的是对象指向的角度。
    下面的方法还能给出长轴和短轴的长度。
'''
(x,y),(MA,ma),angle=cv.fitEllipse(cnt)

'''
6、掩膜和像素点/Mask和PixelPoints
    在某些情况下，我们可能需要获取构成对象的所有像素点。
'''
mask=np.zeros(imgray.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
pixelpoints=np.transpose(np.nonzero(mask))
#pixelpoints=cv.findNonZero(mask)
'''
    上面采用了两种方法来实现。
    Numpy给出的结果是(row,colum)格式的。
    OpenCV给出的格式是(x,y)形式的。
'''

'''
7、最大值和最小值及其位置
    我们可以得到以下参数，通过使用mask图像。
'''
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray,mask = mask)

'''
8、平均颜色及平均灰度
    我们也可以使用相同的mask求一个对象的平均颜色或平均灰度。
'''
mean_val=cv.mean(im,mask=mask)

'''
9、极点
    一个图像中上下左右最边界上的点。
'''
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])