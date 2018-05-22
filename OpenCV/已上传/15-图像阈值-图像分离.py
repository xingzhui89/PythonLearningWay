'''
本节的目标是学习简单阈值，自适应阈值和Otsu's二值化等
主要利用的函数为cv2.threshold,cv2.adaptiveThreshold
'''
'''
    第一种，简单阈值
    当像素值高于阈值是，我们就给这个像素赋予一个新值，否则就赋予另外一只颜色。
    这个函数就是cv2.threshold()。
    def threshold(src, thresh, maxval, type, dst=None):
        .   @param src input array (multiple-channel, 8-bit or 32-bit floating point).
        .   @param dst output array of the same size  and type and the same number of channels as src.
        .   @param thresh threshold value.
        .   @param maxval maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
        .   @param type thresholding type (see the cv::ThresholdTypes).
    举个例子，将一副黑白渐变的图片，按简单阈值进行变换，生成不同风格的图片。
'''

# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/whiteblack.jpg',0)
# ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
#
# titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
#
# images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
#
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

'''
第二种，自适应阈值
在上面一个例子中，我们使用的是全局阈值，使用同一个数对整幅图像进行整理。
但是这种方法并不适应所有的情况，尤其是当同一幅图像上的不同部分具有不同亮度时。
自适应阈值，会根据图像上的每一个小区域计算与其对应的阈值，在不同的区域采用不同的阈值。
def adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None)
    .   @param blockSize Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.
    .   @param C Constant subtracted from the mean or weighted mean (see the details below). Normally, it is positive but may be zero or negative as well.
我们来看一个例子，就能明白与全局阈值的不同之处。
'''

# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/dave.jpg',0)
# #这句代码用于过滤图片中的早点
# img=cv.medianBlur(img,5)
#
# ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
#
# th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
# th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
#
# titles=['Original Image','Global Thresholding(v=127)','Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']
#
# images=[img,th1,th2,th3]
#
# for i in range(4):
#     #subplot(nrows, ncols, plot_number)，如何控制图片排列
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()


'''
第三种方法，Otsu's二值化
在使用全局阈值的时候，我们随便给定了一个数来做阈值，那么如何知道这个数的好坏呢？
对于计算机来说，就是不停的尝试。
一般用于双峰对象，简单来说，就是在直方图中存在两个峰值。
虽然还是使用cv2.threshold()函数，但是需要传入一个cv2.THRESH_OTSU参数，我们把阈值设为0。
然后算法会自动计算最优解，然后返回一个retVal。

'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic/noisy.jpg',0)
ret1,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)

ret2,th2=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

blur=cv.GaussianBlur(img,(5,5),0)
ret3,th3=cv.threshold(blur,2,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()