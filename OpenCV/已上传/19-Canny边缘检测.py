'''
Canny边缘检测是一种非常流行的算法，由以下步骤构成：
1、噪声去除
    第一步是使用5X5的高斯滤波器去除噪声。
2、计算图像梯度
    对平滑后的图像使用Sobel算子计算水平方向和竖直方向的一阶导数。
3、非极大值抑制
    在获取梯度的方向和大小之后，应该对整幅图像做一个扫描，去除哪些非边界上的点。
    对每一个像素进行检查，看这个点的梯度是不是周围具有相通梯度方向的点中最大的。
4、滞后阈值
    现在要确定哪些边界才是真正的边界。
    我们需要设置两个阈值，minVal和maxVal，当图像的灰度梯度高于maxVal时被认为是真的边界。
    低于minVal的边界会被抛弃。

但是在OpenCV中只需要一个函数Canny()就可以完成以上几步。

这个函数的第一个参数是输入图像，第二个和第三个分别是minVal和maxVal。
然后是设置卷积核的大小，默认为3。最后一个参数用来设定求梯度大小的方程,默认为False。
def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None):
    .   @param image 8-bit input image.
    .   @param edges output edge map; single channels 8-bit image, which has the same size as image .
    .   @param threshold1 first threshold for the hysteresis procedure.
    .   @param threshold2 second threshold for the hysteresis procedure.
    .   @param apertureSize aperture size for the Sobel operator.

来看一个实例
'''

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pic/messi.jpg',0)
edges = cv.Canny(img,190,200)#改变这里的阈值，会显示出图片更多或者更少的内容

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

#此处传入图像。