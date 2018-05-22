'''
这里包括的按位操作有： AND， OR， NOT， XOR 等。当我们提取图像的
一部分，选择非矩形 ROI 时这些操作会很有用.
我想把 某部分图像放到另一幅图像上。如果使用加法，颜色会改
变，如果使用混合，会得到透明效果，但是不想要透明。如果这部分图像是矩形我可
以象上一章那样使用 ROI。但是他不是矩形。
所以只能使用按位运算来实现：

我们把绿色的叶子，转移到另一张图上。

后面我们会把所有的图片都截图贴出来，以便大家参考。
'''
import cv2
import numpy as np

#加载图像
img1=cv2.imread('pic/wechat.png')#这是目标图片
img2=cv2.imread('pic/leaf.jpg')#这是我们的绿叶logo
#获取img2的行、列、通道数
rows,cols,channels=img2.shape
#从目标图片中，确定好与leaf大小一致的区域
roi=img1[0:rows,0:cols]

'''
# 彩色转灰度  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
# 灰度转BGR3通道  
color = cv2.cvtColor(grayImg,cv2.COLOR_GRAY2BGR)
'''
#转换成灰度照片
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
'''
def threshold(src, thresh, maxval, type, dst=None)
The function applies fixed-level thresholding to a multiple-channel array. 
-src	input array (multiple-channel, 8-bit or 32-bit floating point).
-dst	output array of the same size and type and the same number of channels as src.
-thresh	threshold value.
-maxval	maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types. 
这个函数的作用就是将灰度图片以某一个阈值作为区分，黑和白变得很明确
小于175的就是0，其他的是255
'''
ret,mask=cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)
#not运算就是将上面的图片进行反转，黑和白转换一下
mask_inv=cv2.bitwise_not(mask)
'''
我们来看一下按位求和运算的函数
def bitwise_and(src1, src2, dst=None, mask=None)
    .   @param src1 first input array or a scalar.
    .   @param src2 second input array or a scalar.
    .   @param dst output array that has the same size and type as the input
    .   arrays.
    .   @param mask optional operation mask, 8-bit single channel array, that
    .   specifies elements of the output array to be changed.
也就是说mask参数，就是用来指定输出矩阵中要改变的元素。
'''
img1_bg=cv2.bitwise_and(roi,roi,mask=mask)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)

dst=cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst

#cv2.imshow('img2gray',img2gray)

#cv2.imshow('mask',mask)
#cv2.imshow('mask_inv',mask_inv)

cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_bg',img2_fg)

cv2.imshow('dst',dst)
cv2.imshow('res',img1)
cv2.imwrite('pic/10-3-1.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()