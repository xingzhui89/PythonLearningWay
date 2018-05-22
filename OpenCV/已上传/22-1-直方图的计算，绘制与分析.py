'''
从今天开始，我们学习直方图。
可以使用OpenCV或者Numpy函数计算直方图。
使用OpenCV或者Matplotlib函数绘制直方图。
'''
'''
原理：
    直方图的概念？通过直方图，我们可以对整幅图像的灰度分布有一个整体的了解。
    直方图的x轴是灰度值（0-225），y轴是图片中具有同一灰度值的点的数组。
    所以直方图就是对图像的另一种解释。
    一定要牢记，直方图是通过灰度图像绘制的，而不是彩色图像。
'''

'''
统计直方图：
    那么如何获取一副图像的直方图呢？
    OpenCV和Numpy都有对应的内置函数。
    BINS：如果我们不需要知道每个像素值的像素点数据，而是希望知道两个像素值之间的像素点数目怎么办？
        比如我们想知道0-15，16-31……，240-255，这样就只需要16个值来绘制直方图，
        取每组的总和。这里的每一个小组就称为BIN。
    DIMS：表示我们收集数据的参数数目，由于我们只使用灰度值，所以为1.
    RANGE：要统计的灰度值范围，一般来说是[0,256]，也就是所有的灰度值。
    
    1、使用OpenCV统计直方图，calcHist函数。
def calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)
    images表示原图像，uint8或者float32格式。当传入函数时需要用[]括起来。
    channels，同样用中括号括起来，他会告诉函数我们要统计哪副图像中的直方图。
        如果输入图像是灰度图，值就是[0].
        如果是彩色图像，传入的参数就可能是[0],[1],[2]。
    mask，掩膜图像。要统计整幅图像的直方图就设为None，如果想统计图像某一部分的画，就需要制作一个掩膜图像。
    histSize，BIN的数组，用[]括起来。
    ranges，像素值的范围，通常为[0,256]
'''
# import cv2
# img=cv2.imread('pic/messi.jpg',0)
# hist=cv2.calcHist([img],[0],None,[256],[0,256])
'''
通过以上代码，我们就获得一个256X1的数组，每一个值代表了与此灰度值对应的像素点数目。
'''
'''
    2、使用Numpy统计直方图，histogram()函数可以帮助统计。
'''
# import numpy as np
# hist,bins=np.histogram(img.ravel(),256,[0,256])
'''
上面的ravel方法，是把图像转成一组数组。
这里计算出来的hist与上面的一样，但是bins是257，因为Numpy的计算方式为0-0.99，1-1.99……

    另外还有一个bincount()方法，运行速度是histogram的十倍。
    对于一维直方图，最好只用这个方法。
'''
# hist=np.bincount(img.ravel(),minlength=256)

'''
绘制直方图：
    有两种方法，ShortWay和LongWay，分别对应Matplotlib和OpenCV函数。
    1、Matplotlib方法，hist()函数。
    可以直接统计并绘制直方图。
'''

# import cv2
# import numpy as np
# import matplotlib.pyplot  as plt
#
# img=cv2.imread('pic/messi.jpg',0)
# plt.hist(img.ravel(),256,[0,256])
# plt.show()

'''
    或者我们只使用matplotlib的绘图功能，在绘制多通道的直方图时，很有用。
    但是首先要告诉绘图函数你的直方图数据在哪里。
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg')
# color=('b','g','r')
#
# for i,col in enumerate(color):
#     histr=cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color=col)
#     plt.xlim(0,256)
# plt.show()
# ###此处插入图片22-1-2
'''
使用掩膜mask：
    要统计图像某个局部区域的直方图只需要构建一副掩膜图像。
    将要统计的部分设置为白色，其余部分为黑色，即可。
    把这个掩膜图像传递给函数就可以了
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic/messi.jpg',0)
mask=np.zeros(img.shape[:2],np.uint8)
mask[100:200,100:250]=255
masked_img=cv2.bitwise_and(img,img,mask=mask)

hist_full=cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask=cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()
####此处插入图22-1-3