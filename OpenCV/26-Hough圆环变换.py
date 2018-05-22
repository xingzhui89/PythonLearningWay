'''
学习使用霍夫变换在图像中找圆形或圆环
使用到的函数为cv2.HoughCircles()

原理：
    圆形的数学表达式为(x−xcenter)2+(y−ycenter)2=r2
    其中(xcenter,ycenter)表示圆心的坐标，r表示半径。
    所以一个圆环需要3个参数来确定，进行圆形霍夫变换的累加器必需是3维的。
    这样的话效率很低，所以OpenCV采用了一个比较巧妙的方法，霍夫梯度法。
    使用边界的梯度信息。
    def HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
    .   @param param1 First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the higher
         threshold of the two passed to the Canny edge detector (the lower one is twice smaller).
    .   @param param2 Second method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the
        accumulator threshold for the circle centers at the detection stage. The smaller it is, the more
        false circles may be detected. Circles, corresponding to the larger accumulator values, will be
        returned first.
    .   @param circles Output vector of found circles. Each vector is encoded as a 3-element
    .   floating-point vector (x, y, radius) .
    返回值是一个向量，包含 x,y和radius。
    param2,这个参数如果太小的话，就会出现一些检测错误。
    这里不展开介绍了。
'''
import cv2
import numpy as np
img=cv2.imread('pic/OpenCVlogo.jpg',0)
img=cv2.medianBlur(img,5)
cimg=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,30,param1=50,param2=45,minRadius=0,maxRadius=0)
circles=np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('pic/26-1.jpg',cimg)
#插入图片26-1