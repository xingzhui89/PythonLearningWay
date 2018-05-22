'''
今天主要介绍如何使用opencv读入一幅图像，如何显示图像，以及如何保存图像。
'''
import cv2
import numpy as np
'''
如何读入图像
使用函数cv2.imread(filepath,flags)函数读入图像，只要该图像在此程序的工作路径，或者给出完整路径。
第二个参数则是要告诉函数应该如何读取这幅图片。
    filepath：要读入图片的完整路径
    flags：读入图片的标志
        cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
        cv2.IMREAD_GRAYSCALE：读入灰度图片
        cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
'''
img=cv2.imread('pic/me.jpg',cv2.IMREAD_COLOR)

'''
如何显示图像
使用函数cv2.imshow(wname,img)显示图像，
第一个参数是显示图像的窗口的名字,可以创建多个窗口，但是务必给出不同的名字
第二个参数是要显示的图像（imread读入的图像），窗口大小自动调整为图片大小


    cv2.waitKey()顾名思义等待键盘输入，单位为毫秒，即等待指定的毫秒数看是否有键盘输入，
        若在等待时间内按下任意键则返回按键的ASCII码，程序继续运行。
        若没有按下任何键，超时后返回-1。参数为0表示无限等待。不调用waitKey的话，窗口会一闪而逝，看不到显示的图片。
    cv2.destroyAllWindow()销毁所有窗口
    cv2.destroyWindow(wname)销毁指定窗口
如果我们想调节窗口的大小，我们可以先创建一个窗口，之后再加载图像。
这时使用的是cv2.namedWindow()函数，选择WINDOW_NORMAL标签，就可以调整窗口大小了。
'''
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
保存图像
使用函数cv2.imwrite(file，img，num)保存一个图像。
第一个参数是要保存的文件名，
第二个参数是要保存的图像。
可选的第三个参数，它针对特定的格式：对于JPEG，其表示的是图像的质量，用0 - 100的整数表示，默认95;对于png ,第三个参数表示的是压缩级别。默认为3.
'''
cv2.imwrite('test.png',img)


