'''
本节要介绍的是图像梯度，图像边界等概念。
使用到的函数有Sobel(),Scharr(),Laplacian()等。

梯度简单来说就是求导。
OpenCV提供了三种不同的梯度滤波器，Sobel,Scharr,Laplacian。

1、Sobel算子和Scharr算子
    Sobel算子是高斯平滑和微分操作的结合，所以抗噪能力很好。
    可以设置求导的方向xorder或者yorder，还可以设定使用的卷积核的大小ksize。
    如果ksize=-1，会使用3x3的Scharr滤波器，效果更好。
    x方向[[-3,0,3],[-10,0,10],[-3,0,3]]
    y方向[[-3,-10,-3],[0,0,0],[3,10,3]]

2、Laplacian算子
    拉普拉斯算子可以使用二阶导数的形式定义。其离散实现类似于二阶Sobel导数。
    计算公式略过。。。

我们来看一个实例，看看几种算法的不同之处。
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic/dave.jpg',0)

laplacian=cv.Laplacian(img,cv.CV_64F)

sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)

sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1), plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian,cmap='gray')
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx,cmap='gray')
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely,cmap='gray')
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])
plt.show()

'''
传入上面例子的图片

另外需要着重关注的一点是，我们可以通过参数-1来设定输出图像的深度（数据类型）与原图保持一直，但是我们更倾向于使用更高的数据类型。
以免丢失图像边界。

'''