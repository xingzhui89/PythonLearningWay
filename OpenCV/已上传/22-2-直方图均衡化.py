'''
如果一副图像中的大多数像素点的像素值都集中在一个像素值范围之内会怎样呢？
比如，一副图片整体很亮，那么所有的像素值应该都会很高。
但是一副高质量的图像的像素值分布应该很广泛，所以应该把其直方图做一个横向拉伸。
这就是直方图均衡化要做的事情。
通常，这种操作会改善图像的对比度。
一、我们先来看看Numpy中是如何处理的
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img=cv2.imread('pic/wiki.jpg',0)
# hist,bins=np.histogram(img.flatten(),256,[0,256])
# cdf=hist.cumsum()
# cdf_normalized=cdf*hist.max()/cdf.max()
#
# plt.subplot(211),plt.imshow(img,'gray')
# plt.subplot(212),plt.plot(cdf_normalized,color='b')
# plt.hist(img.flatten(),256,[0,256],color='r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'),loc='upper left')
# plt.show()
# ###此处插入图片22-2-1
'''
从上图中可以看出，直方图大部分都集中在灰度值较高的地方，而且很集中。
我们希望直方图的分布比较分散，能够覆盖整个x轴。
所以需要一个变换函数帮助我们把现在的直方图映射到一个广泛分布的直方图中。
这就是直方图均衡化要做的事情。
我们现在要找到直方图中的最小值，除了0，并把它用于wiki中的直方图均衡化公式。

'''
# cdf_m=np.ma.masked_equal(cdf,0)
# cdf_m=(cdf_m-cdf_m.min())*255/(cdf_m.max(-cdf_m.min()))
#
# cdf=np.ma.filled(cdf_m,0).astype('uint8')
#
# img2=cdf[img]
#
# plt.subplot(211),plt.imshow(img2,'gray')
# plt.subplot(212),plt.plot(cdf,color='b')
# plt.hist(img2.flatten(),256,[0,256],color='r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'),loc='upper left')
# plt.show()
# ###此处插入图片22-2-2
'''
另外一个比较重要的特点是，即使我们的输入图片比较暗，在经过直方图均衡化之后，也能得到相同的结果。
'''

'''
二、OpenCV中的直方图均衡化
    equalizeHist()函数，输入图片仅仅是一副灰度图像，输出结果是直方图均衡化之后的图像。
'''
# img=cv2.imread('pic/wiki.jpg',0)
# equ=cv2.equalizeHist(img)
# res=np.vstack((img,equ))
# cv2.imwrite('pic/wiki_res.jpg',res)
#
# plt.subplot(121),plt.imshow(img,'gray')
# plt.subplot(122),plt.imshow(equ,'gray')
# plt.show()
# ##此处插入图片，wiki_res
'''
    所以当直方图中的数据集中在某一个灰度值范围内时，直方图均衡化很有用。
'''

'''
三、有限对比适应性直方图均衡化
    有时候，我们使用上面方式做的直方图均衡化，虽然可以改变对比度，但是有时候会丢失一些信息
    比如一张图片变得太亮，导致信息丢失。
    为了解决这中问题，我们需要使用自适应的直方图均衡化。
    其原理为：
        将图像分成很多小块，然后对每个小块进行直方图均衡化。
'''

img=cv2.imread('pic/diaosu.jpg',0)
clahe=cv2.createCLAHE(clipLimit=2.0,titleGridSize=(8,8))
cl1=clahe.apply(img)

cv2.imwrite('pic/diaosu_res.jpg',0)

