'''
这一节将介绍如何对图像进行颜色空间转换，比如从BGR到灰度图，或者从BGR到HSV。
并且要创建一个程序，如何从一个video中提取一个有颜色的物体。
主要介绍的函数包括cv.cvtColor(),cv.inRange()等

OpenCV中有150种color-space的转换方法，但是我们主要介绍BGR->Gray以及BGR->HSV.

cv.cvtColor(input_image, flag)
这是我们主要的转换函数。
其中flag有很多，我们来获取一下所有的flag。
常用的是cv.COLOR_BGR2GRAY,cv.COLOR_BGR2HSV
'''
import cv2 as cv
flags=[i for i in dir(cv) if i.startswith('COLOR_')]
print(len(flags),flags)

'''
物体跟踪
在HSV颜色空间中要比在BGR空间中更容易表示一个特定颜色。
假如我们要提取一个蓝色的物体。
具体实现程序步骤如下：
1、从视频中获取一帧图像
2、将图像转换到HSV空间
3、设置HSV阈值到蓝色范围
4、获取蓝色物体，当然还可以多做一些额外的事情。
代码实现：
'''

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

while(True):
    #这句很好理解，通过摄像头来获取图像
    ret,frame=cap.read()
    #将BGR图像转换成HSV图像
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #设置蓝色的提取范围
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    '''
    def inRange(src, lowerb, upperb, dst=None)
    Checks if array elements lie between the elements of two other arrays.
    检查矩阵元素是否在某个范围之间。
    .   @param src first input array.
    .   @param lowerb inclusive lower boundary array or a scalar.
    .   @param upperb inclusive upper boundary array or a scalar.
    .   @param dst output array of the same size as src and CV_8U type.
    mask是一个包含0和非零数的矩阵
    '''
    mask=cv.inRange(hsv,lower_blue,upper_blue)
    #print(mask)
    #在mask不为0的地方，进行and操作
    res=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k=cv.waitKey(5)
    if k==27:
        break

cv.destroyAllWindows()

'''
BGR和HSV的转换如何实现？
1、一种方法是通过在线转换工具，可以把BGR转换成HSV，也可以把自己想要的所有颜色转换成HSV。
2、代码形式，我们自定义一个BGR对象，然后通过cv.cvtColor函数实现。然后确定上下阈值。

'''

