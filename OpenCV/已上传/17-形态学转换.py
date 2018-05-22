'''
今天介绍不同的形态学操作，例如腐蚀，膨胀，开运算，闭运算等。
主要涉及的函数包括erode(),dilate(),morphologyEx()。

形态学操作是根据图像形状进行的简单操作。
一般情况下对二值化图像进行操作，需要输入两个参数，一个是原始图像，另一个就是结构化元素或核。

'''

'''
1、腐蚀
    这种操作会把前景物体的边界腐蚀掉。
    卷积核沿着图像滑动，如果与卷积核对应的原图像的所有像素值都是1，那么中心元素就保持原来的像素值。
    否则就变为0.
    根据这个道理，靠近前景的所有像素都会被腐蚀掉，所以前景物体会变小，整幅图像的白色区域会减少。
    
举个例子来说明，使用5x5的归一化卷积核。
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic/j.png',0)
kernel=np.ones((5,5),np.uint8)
erosion=cv.erode(img,kernel,iterations=1)

plt.subplot(121),plt.imshow(img),plt.title('IMG')
plt.subplot(122),plt.imshow(erosion),plt.title('EROSION')
plt.show()

#插入图片17-1

'''
2、膨胀
    与腐蚀相反的，假如与卷积核对应的原图像的像素值中只要有一个是1，中心元素的像素值就是1.
    所以这个操作会增加白色区域。
    一般先用腐蚀，去除白噪声，然后再进行膨胀。
    还是以上面那个图像说明。
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic/j.png',0)
kernel=np.ones((5,5),np.uint8)
erosion=cv.dilate(img,kernel,iterations=1)

plt.subplot(121),plt.imshow(img),plt.title('IMG')
plt.subplot(122),plt.imshow(erosion),plt.title('EROSION')
plt.show()

#插入图片17-2
'''
3、开运算
    先进行腐蚀，再进行膨胀就叫做开运算。
    用于去除噪声。
    使用morphologyEx()函数。
    除了原始图片和卷积核之外，还需要传入op参数。
    @param op Type of a morphological operation
'''
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
plt.subplot(121),plt.imshow(img),plt.title('IMG')
plt.subplot(122),plt.imshow(opening),plt.title('OPENING')
plt.show()
#插入17-3

'''
4、闭运算
    先膨胀，再腐蚀，经常用于填充前景物体中的斑点。
'''
# closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

'''
5、形态学梯度
    就是一副图像腐蚀和膨胀之间的区别，结果看起来像是物体的轮廓。
'''
# gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

'''
6、Top Hat
    描述的是图像的开运算和输入图像之间的差别。
'''
# tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

'''
7、Black Hat
    描述的是图像的闭运算和输入图像的区别。
'''
# blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

'''
结构化元素
之前我们一直在使用Numpy创建结构化元素，都是矩形的。
但是在一些情况下，我们需要渐变或者环形的卷积核，OpenCV提供了getStructuringElement()方法。
传入形状和核的大小即可。
'''
# Rectangular Kernel
# cv.getStructuringElement(cv.MORPH_RECT,(5,5))
'''
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
'''
# Elliptical Kernel
# cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
'''
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
'''

# Cross-shaped Kernel
# cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
'''
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
'''