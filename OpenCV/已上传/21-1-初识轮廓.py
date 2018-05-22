'''
一、什么是轮廓？
    轮廓可以简单的认为成将连续的点连在一起的曲线，具有相同的颜色或者灰度。
    轮廓在形状分析或者物体的检测和识别中很有用。
    ·为了更加准确，需要使用二值化图像，在寻找轮着之前，要进行阈值化处理或者Canny边界检测。
    ·查找轮廓的函数会修改原始图像，如果在找到轮廓之后还想使用原始图像，应该将原始图像存储到其他变量中。
    ·在OpenCV中，查找以轮廓就像在黑色背景中找白色物体。所以背景是黑色，前景是白色。
我们来看一下如何查找一个二值化图片的轮廓。
'''
import numpy as np
import cv2 as cv
im=cv.imread('pic/messi.jpg')
imgray=cv.cvtColor(im,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(imgray,127,255,0)
im2,contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
'''
在findContours()函数中有三个参数，第一个是原图片，第二个是轮廓检查模式，第三个参数是轮廓近似方法。
这个方法输出三个结果，一个是修改后的图像，一个是轮廓，在一个是层析结构。
在第二个返回值轮廓中，包含的是这个图像中所有轮廓组成的列表。每一个轮廓都是一个Numpy数组，包含边界点(x,y)的坐标。
'''

'''
二、如何绘制轮廓
    drawContours()可以用来绘制轮廓。
    它根据提供的边界点绘制任何形状。
    接收的第一个参数是原始图像，第二个参数是轮廓（列表形式），第三个参数是轮廓的索引（-1表示绘制所有轮廓）。
    还有一些参数是轮廓的颜色和厚度等。
'''
#绘制一副图像中所有的轮廓
cv.drawContours(im,contours,-1,(0,255,0),3)
#绘制一副图像中个别轮廓，比如第4层。
cv.drawContours(im,contours,3,(0,255,0),3)
#但是大部分情况下，我们使用下面的方法，虽然与上面相同的结果，但是更有效：
cnt=contours[4]
cv.drawContours(im,[cnt],0,(0,255,0),3)

'''
三、轮廓的近似方法Contour Approximation Method 
    这是函数findCountours()的第三个参数。这个参数有什么作用？
    在前面，我们讲过轮廓是具有相同强度值的形状的边界。
    它会存储形状边界上所有的(x,y)坐标。但是需要将所有的这些边界点都存储下来么？
    这就是该参数要传递给findContours的信息。
    如果参数值设置为CHAIN_APPROX_NONE，所有的边界点都会被存储。
    但是当我们的边界比较简单，比如只有一条直线，我们只需要两点即可。
    此时参数值应该设置为CHAIN_APPROX_SIMPLE,能够去除冗余点，压缩轮廓，从而节省内存开支。
    
'''