'''
3、形状匹配
    matchShape()方法可以帮助我们比较两个形状或轮廓的相似度。
    如果返回值越小，匹配越好。
    原理是根据Hu矩来计算的。
    我们看一个具体的比较案例：
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('pic/star.jpg',0)
img2=cv2.imread('pic/star2.jpg',0)

ret,thresh=cv2.threshold(img1,127,255,0)
ret,thresh2=cv2.threshold(img2,127,255,0)

_,contours,hierarchy=cv2.findContours(thresh,2,1)
cnt1=contours[0]

_,contours,hierarchy=cv2.findContours(thresh2,2,1)
cnt2=contours[0]

ret=cv2.matchShapes(cnt1,cnt2,1,0.0)
#0.00451512584549435,相似度并不低哦，0表示相似度最高，数值越小相似度越高。

print(ret)

plt.subplot(121),plt.imshow(img1),plt.title('IMG1')
plt.subplot(122),plt.imshow(img2),plt.title('IMG2')
plt.show()

# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
# cv2.imshow('ret',ret)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
    这里要说明的是，Hu矩是归一化中心矩的线性组合，之所以这样就是为了能够获取
代表图像的某个特征的矩函数。这些矩函数对于某些变化，如缩放，旋转，镜像映射具有不变形的特点。
'''