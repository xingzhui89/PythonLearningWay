'''
关于轮廓的其他一些函数，包括：
凸缺陷，以及如何寻找凸缺陷；
找某一点到一个多边形的最短距离
不同形状的匹配
'''
import cv2
import numpy as np
'''
1、凸缺陷
    前面讲过，对象上的任何凹陷都被称为凸缺陷。
    OpenCV中的convexityDefect()函数可以帮助我们找到凸缺陷
    该函数会返回一个数组，每一行包含的值为[起点，终点，最远的点，到最远点的近似距离]。
    我们可以在一张图上显示它。我们将起点和终点连接起来，然后在最远点画一个圆弧。
    请记住，前三个数值返回的是轮廓点的索引，还需要在轮廓点中确认。
'''
#hull=cv2.convexHull(cnt,returnPoints=False)
#defects=cv2.convexityDefects(cnt,hull)
'''
    如果要查找凸缺陷，在使用convexHull寻找凸包时，returnPoints参数要设为False。
    下面我们还是以之前的星星图片为例，介绍一下代码。
'''
img=cv2.imread('pic/star.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,127,255,0)
'''
Traceback (most recent call last):
  File "D:/Python Mat/codes/simplecode/OpenCV/21-4-1-关于轮廓的更多函数.py", line 26, in <module>
    contours,hierarchy=cv2.findContours(thresh,2,1)
ValueError: too many values to unpack (expected 2)
'''
_,contours,hierarchy=cv2.findContours(thresh,2,1)
cnt=contours[0]

hull=cv2.convexHull(cnt,returnPoints=False)
defects=cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]
    start=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

cv2.imshow('img',img)
cv2.imwrite('pic/21-4-1.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#此处可以插入结果图片

'''
2、Point Polygon Test
    该方法表示求解图像中的一个点到一个对象轮廓的最短距离。
    如果点在轮廓的外部，返回值为负；
    如果在点在轮廓上，返回值为0；
    如果点在轮廓内部，返回值为正。
'''
# dist=cv2.pointPolygonTest(cnt,(50,50),True)
'''
    第三个参数是measureDist，如果设置为True，表示计算最短距离。
    如果设置为False，只会判断这个点和轮廓之间的位置关系。
    如果我们不需要知道具体距离，那么设置为False可以提高2-3倍计算速度。
'''
