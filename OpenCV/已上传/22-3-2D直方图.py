'''
简单的介绍一下如何计算和绘制2D直方图。

前面我们绘制的都是一维直方图，因为我们只考虑了图像的一个特征：灰度值。
但是在2D直方图中，我们要考虑两个图像特征，颜色和饱和度。根据这两个特征绘制2D直方图。

1、在OpenCV中，使用函数calcHist()来计算直方图简单方便。
如果要绘制颜色直方图的画，需要将图像的颜色空间从BGR转换到HSV。
函数参数也要做一些修改：
    channels=[0,1]，同时处理H和S两个通道。
    bins=[180,256]，H通道为180，S通道为256.
    range=[0,180,0,256]，H的取值范围和S的取值范围。
'''
# import cv2
# import numpy as np
#
# img=cv2.imread('pic/messi.jpg')
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
# hist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
#
# cv2.imwrite('pic/22-3-1.jpg',hist)
# cv2.imshow('hist',hist)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
2、Numpy中的2D直方图函数，np.histogram2d()。
请参看下面的代码。
第一个参数时H通道，第二个参数是S通道，第三个参数是bins的数目，第四个参数是数值范围。

'''
# import matplotlib.pyplot as plt
# img=cv2.imread('pic/messi.jpg')
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# h,s=np.indices(hsv.shape[:2])
# hist,xbins,ybins=np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

'''
2、如何将2D直方图绘制出来
    只用cv2.imshow()方法得到的是一个180X256的量为数组。但是这个图是灰度图。
    出入我们知道不同颜色H通道的值，否则我们不知道那到底代表什么颜色。
    
    使用matplotlib中的imshow()方法来绘制2D直方图，再配合不同的颜色图。
    这样我们会对每个点所代表的数值大小有一个更直观的认识。
    比较简单好看，但是我们还是不知道数字代表的颜色是什么。
'''
# img=cv2.imread('pic/messi.jpg')
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# hist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
# # cv2.imwrite('pic/22-3-2.jpg',hist)
# plt.imshow(hist,interpolation='nearest')
# plt.show()

'''
    上面的图中，X轴显示S值，Y轴显示H值。
    
3、OpenCV风格的案例
    在官方文档中有一个关于颜色直方图的例子。
    我们看一下代码。可以实现颜色直方图显示对应的颜色。
'''
import numpy as np
import cv2

if __name__=='__main__':
    hsv_map=np.zeros((180,256,3),np.uint8)
    h,s=np.indices(hsv_map.shape[:2])
    hsv_map[:,:,0]=h
    hsv_map[:,:,1]=s
    hsv_map[:,:2]=255
    hsv_map=cv2.cvtColor(hsv_map,cv2.COLOR_HSV2BGR)
    cv2.imshow('hsv_map',hsv_map)

    cv2.namedWindow('hist',0)
    hist_scale=10
    def set_scale(val):
        global hist_scale
        hist_scale=val
    cv2.createTrackbar('scale','hist',hist_scale,32,set_scale)
    cam=cv2.VideoCapture(0)
    while(cam.isOpened()):
        ret,frame=cam.read()
        cv2.imshow('camera',frame)
        small=cv2.pyrDown(frame)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dark=hsv[:,:,2]<32
        hsv[dark]=0
        h=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
        h=np.clip(h*0.005*hist_scale,0,1)
        vis=hsv_map*h[:,:,np.newaxis]/255.0
        cv2.imshow('hist',vis)

        ch=cv2.waitKey(1)
        if ch==27:
            break
    cv2.destroyAllWindows()