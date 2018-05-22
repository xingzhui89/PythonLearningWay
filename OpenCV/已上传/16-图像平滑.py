'''
图像平滑
通过学习不同的低通滤波器，对图像进行模糊
使用自定义的滤波器对图像进行卷积（2D卷积）
'''
'''
2D卷积，图像过滤
与一维信号一样，可以对2D图像实施低通滤波LPF，高通滤波HPF等。
LPF帮助我们去除噪音，模糊图像。
HPF帮助我们找到图像中的边界。
OpenCV提供了filter2D()函数，让我们对一副图像进行卷积操作。
def filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None):
    .   @param src input image.
    .   @param dst output image of the same size and the same number of channels as src.
    .   @param ddepth desired depth of the destination image, see @ref filter_depths "combinations"
    .   @param kernel convolution kernel (or rather a correlation kernel), a single-channel floating point
    .   matrix; if you want to apply different kernels to different channels, split the image into
    .   separate color planes using split and process them individually.
    .   @param anchor anchor of the kernel that indicates the relative position of a filtered point within
    .   the kernel; the anchor should lie within the kernel; default value (-1,-1) means that the anchor
    .   is at the kernel center.
    .   @param delta optional value added to the filtered pixels before storing them in dst.
    .   @param borderType pixel extrapolation method, see cv::BorderTypes
下面举个例子，对一副图像使用平均滤波器。比如使用一个10x10的平均滤波器核。
操作方法：将核放在图像的一个像素A上，求与核对应的图像上100个像素的和，再取平均数。
用这个平均数替代A的值。
重复以上操作，直到将图像的每一个像素值都更新一遍。
看具体的代码实现：
'''

# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/OpenCVlogo.jpg')
# kernel=np.ones((10,10),np.float32)/100
#
# #when ddepth=-1, the output image will have the same depth as the source
# dst=cv.filter2D(img,-1,kernel)
#
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()


'''
使用低通滤波器可以达到图像模糊的目的，就是去除图像中的高频成分，有时候边界也会被模糊一点。
OpenCV中提供了四种模糊技术
1、平均
    由归一化卷积框来实现。用卷积框覆盖区域所有像素的平均值来代替中心元素。
    可以使用blur()和boxFilter()函数来完成这个任务。
    我们需要做的就是设定卷积框的宽和高，比如3x3的归一化卷积框。
    def blur(src, ksize, dst=None, anchor=None, borderType=None):
    .   @param ksize blurring kernel size.
    如果不想使用归一化卷积框，可以用boxFilter()，需要传入参数normalize=False来实现。
    第一部分的那个例子还可以这么来写：
'''

# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/OpenCVlogo.jpg')
# blur = cv.blur(img, (9, 9))#这里可以尝试，数字越大，图像越模糊。
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

'''
2、高斯模糊
    把卷积核换成高斯核，也就是方框不变，但是将原来每个方框的值变成是符合高斯分布的。
    方框中心的值最大，其余方框根据距离中心元素的距离递减，构成一个高斯小山包。
    原来求平均数，现在变成求加权平均数。
    通过GaussianBlur()来实现。我们需要指定高斯核的宽和高，必须是奇数。
    以及沿X，Y方向的标准差，如果设置为0，那么函数会自己进行计算。
'''
#blur=cv.GaussianBlur(img,(5,5),0)

'''
3、中值模糊
    用于卷积框对应像素的中值来替代中心像素的值。
    卷积核的大小应该设置为奇数。
'''
#median=cv.medianBlur(img,5)

'''
4、双边滤波
    在保持边界清晰的情况下有效的去除噪音。
    但是效率比较慢。
    双边滤波在同时使用空间高斯权重和灰度值相似性高斯权重。
    空间高斯函数确保只有临近区域的像素对中心点有影响。
    灰度相似性高斯函数确保只有与中心像素灰度值相近的才会被用来做模糊运算。
'''
# blur=cv.bilateralFilter(img,9,75,75)
