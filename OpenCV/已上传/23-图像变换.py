'''
1、傅里叶变换
    傅里叶变换经常被用来分析不同滤波器的频率特性。
    我们可以使用2D离散傅里叶变换DFT分析图像的频域特性。
    实现DFT的一个快速算法被称为快速傅里叶变换，FFT。

    假设对于一个正弦信号：x(t)=Asin(2pift),其频率为f。
    如果把这个信号转到其频率表示，我们会在频率f中看到一个峰值。
    如果信号是由采样产生的离散信号组成，我们会得到类似的频谱图。
    如果我们把一张图像想象成沿着两个方向采集的信号，所以对图像同时进行X和Y方向
的傅里叶变换，就可以得到图片的频域显示（频谱图）。
    如果信号的变化幅度非常快，可以说是高频信号；如果变化非常慢，我们称为低频信号。
    如果图像中的变化幅度很大，就是边界点或者噪声。
    所以我们说噪声是图像中的高高频分量，这里是变化快，而不是数量多。

2、Numpy中的傅里叶变换
    Numpy中的FFT包可以帮助我们实现快速傅里叶变换。
    np.fft.fft2()可以对信号进行频率转换，得到一个复杂的数组。
    第一个参数是输入图像，需要是灰度格式。
    第二个参数是可选的，决定输出数组的大小。
    输出输入数组大小应该是一样的。如果设置为输出大，输入图像需要在FFT前补0.
        如果输出小，输入图像被切割。
    假设已经得到了结果，频率为0的部分（直流分量）在输出图像的左上角。
    如果想让它显示在输出图像的中心，我们还需要将结果沿两个方向平移N/2.
    np.fft.fftshift()可以帮助我们实现这一步。
    然后我们就可以构建振幅谱了。
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg',0)
# f=np.fft.fft2(img)
# fshift=np.fft.fftshift(f)
#
# magnitude_spectrum=20*np.log(np.abs(fshift))
#
# plt.subplot(121),plt.imshow(img,cmap='gray')
# plt.title('Input Image'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum,cmap='gray')
# plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
# plt.show()
# ###此处插入图片23-1
'''
    从上图中可以看到，输出结果的中心部分更白，说明低频分量更多。
    现在我们可以进行频域变换了，我们就可以在频域对图像进行一些操作。
    例如高通滤波和重建图像（DFT的逆变换）。
    比如我们使用一个60X60的矩形窗口对图像进行掩膜操作从而去除低频分量。
    然后再使用函数np.fft.ifftshift()进行逆平移操作，所以现在直流分量又回到左上角了。
    然后使用np.ifft2()进行FFT逆变换。同样得到一堆复杂的数字，取绝对值。
    沿用上面的部分程序，请自行参考。
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg',0)
# f=np.fft.fft2(img)
# fshift=np.fft.fftshift(f)
# rows,cols=img.shape
# crow,ccol=int(rows/2),int(cols/2)
# fshift[crow-30:crow+30,ccol-30:ccol+30]=0
# f_ishift=np.fft.ifftshift(fshift)
# img_back=np.fft.ifft2(f_ishift)
#
# img_back=np.abs(img_back)
#
# plt.subplot(131),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
# plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(img_back)
# plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
# plt.show()
# ##此处插入图片23-2
'''
    从上图可以看出，高通滤波其实是一种边界检测操作。
    然后我们再看一下OpenCV中是如何进行这些操作的。
    
3、OpenCV中的傅里叶变换
    对应的函数是cv2.dft()和cv2.idft()，输出结果是双通道的。
    第一个通道是结果的实数部分，第二个通道是结果的虚数部分。
    输入图像要首先转换称np.float32格式。
    我们直接来看实现代码：
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg',0)
# dft=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift=np.fft.fftshift(dft)
#
# magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()
# ##此处插入图片23-3，基本上与前面的-1图片相同
'''
    然后我们可以来做逆DFT，在前面的部分我们实现了一个HPF（高通滤波）。
    我们现在来做LPF（低通滤波）将高频部分去除。其实就是对图像进行模糊操作。
    首先我们需要构建一个掩膜，与低频区域对应的地方设置为1，与高频区域对应的地方设置为0.
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg',0)
# dft=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift=np.fft.fftshift(dft)
#
# rows,cols=img.shape
# crow,ccol=np.uint8(rows/2),np.uint8(cols/2)
#
# mask=np.zeros((rows,cols,2),np.uint8)
# mask[crow-30:crow+30,ccol-30:ccol+30]=1
#
# fshift=dft_shift*mask
# f_ishift=np.fft.ifftshift(fshift)
# img_back=cv2.idft(f_ishift)
# img_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
#
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()
# ##此处插入图片23-4

'''
4、DFT的性能优化
    当数组的大小为某些值时，DFT的性能会更好。比如数组的大小是2的指数时，效率最高。
    我们可以修改输入图像的大小，通过补0的方式。
    OpenCV提供了一个函数getOptimalDFTSize()用于确定最佳大小。
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg',0)
# rows,cols=img.shape
# print(rows,cols)
#
# nrows=cv2.getOptimalDFTSize(rows)
# ncols=cv2.getOptimalDFTSize(cols)
# print(nrows,ncols)
#
# nimg=np.zeros((nrows,ncols))
# nimg[:rows,:cols]=img
