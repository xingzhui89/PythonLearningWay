'''
这里要介绍的是如何查找轮廓的不同特征，比如面积，周长，重心，边界框等。
我们介绍一些轮廓相关参数。

1、矩
    图像的矩可以帮助我们计算图像的质心，面积等。
    moments()方法会将计算得到的矩以一个字典的形式返回。
'''
import cv2
import numpy as np

img=cv2.imread('pic/star.jpg',0)
ret,thresh=cv2.threshold(img,127,255,0)
_,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#note Since opencv 3.2 source image is not modified by this function.
#啥，原图像不会被修改了？
#一开始返回两个参数报错，ValueError.
#### 原因：由于版本（使用的时3.2.0.7）问题 cv.findContours返回值个数发生变化，变为3个。
####如果第一个参数不使用的话，可以用下划线代替。

cnt=contours[0]
M=cv2.moments(cnt)
# print(M)
for key,value in M.items():
    print(key,value)

# cv2.imshow('img',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
通过上面计算得到的矩的值，我们可以计算出对象的重心。
'''
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,cy)#399 720

'''
2、轮廓面积
    轮廓的面积可以使用函数contourArea()计算得到，也可以使用矩（0阶矩），M['m00'].
    area=cv2.contourArea(cnt)
    
3、轮廓周长
    也即弧长，可以使用函数arcLength()计算得到。
    该函数的第二参数可以用来指定对象的形状是True闭合，还是打开的。
    perimeter=cv2.arcLength(cnt,True)
    
4、轮廓近似
    将轮廓形状近似到另外一种由更少点组成的轮廓形状。
    新轮廓的点的数目由我们设定的准确度来决定。
    使用Douglas-Peucker算法。
    假设我们要在一副图像中查找一个矩形，但是由于图像的种种原因，
我们不能得到一个完美的矩形，而是一个‘坏形状’，比如说得到很多折线组成的图形。
    这时候，我们就可以利用近似函数。
    
    如下面代码所示：
    epsilon表示从轮廓到近似轮廓中间的最大距离。
    这是一个准确度参数，对于得到满意结果很有帮助。
    approxPolyDP的第三个参数用于设定弧线是否闭合。
'''
epsilon=0.1*cv2.arcLength(cnt,True)
approx=cv2.approxPolyDP(cnt,epsilon,True)

'''
5、凸包
    与轮廓相似，但不同。有些情况下给出的结果是一样的。
    convexHull()函数用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷。
    一般来说，凸性曲线总是凸出来的，至少是平的。如果由地方凹进去，就被叫做凸性缺陷。
    比如一只手，手指间的凹陷，就是一种凸性缺陷。
def convexHull(points, hull=None, clockwise=None, returnPoints=None):
    points，表示要传入的轮廓
    hull，输出的内容，一般不需要
    clockwise，方向标志。True表示顺时针输出。
    returnPoints，默认为True，会返回凸包上点的坐标。
        如果设置为False，会返回与凸包点对应的轮廓上的点。注意不是坐标。
        所以说如果想要获得凸性缺陷，就要设置这个参数为False。
'''
hull=cv2.convexHull(cnt)

'''
6、凸性检测
    isContourConvex()函数可以用来检测一个曲线是不是凸的。
'''
k=cv2.isContourConvex(cnt)

'''
7、边界矩形
    第一种是：直边界矩形，不会考虑对象是否旋转。所以边界矩形的面积不是最小的。
    可以通过boundingRect()查找得到。
'''
x,y,w,h=cv2.boundingRect(cnt)
img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
'''
    第二种是：旋转的边界矩形，这种矩形的面积是最小的，因为它考虑了对象的旋转。
    用到的函数为minAreaRect()，返回一个Box2D结构。
    其中包含中心点坐标(x,y)，矩形的宽和高(w,h)，以及旋转角度。
    为了画这个矩形，我们需要矩形4个角点的坐标。可以通过boxPoints()获取。
'''
rect=cv2.minAreaRect(cnt)
box=cv2.boxPoints(rect)
box=np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

'''
8、最小外接圆
    minEnclosingCircle()可以找到一个对象的外接圆。
'''
(x,y),radius=cv2.minEnclosingCircle(cnt)
center=(int(x),int(y))
radius=int(radius)
img=cv2.circle(img,center,radius,(0,255,0),2)
'''
9、椭圆拟合
    使用的函数为ellipse()，返回旋转的矩形的内切椭圆。
'''
ellipse=cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(0,255,0),2)

'''
10、直线拟合
    我们可以根据一组点拟合出一条直线，对于一组白色点的图像，我们也能近似的拟合出一条直线来。
'''
rows,cols=img.shape[:2]
[vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
lefty=int(y-(x*vy/vx))
righty=int(y+(cols-x)*vy/vx)
cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)


