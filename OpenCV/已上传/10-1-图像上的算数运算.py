'''
学习图像上的算数运算，加法，减法，位运算
cv2.add(),cv2.addWeighted()等
'''

import cv2
import numpy as np

'''
你可以使用函数 cv2.add() 将两幅图像进行加法运算，当然也可以直接使
用 numpy， res=img1+img。两幅图像的大小，类型必须一致，或者第二个
图像可以使一个简单的标量值。
'''
x=np.uint8([250])
y=np.uint8([10])
#OpenCV 的加法是一种饱和操作，而 Numpy 的加法是一种模操作
print(cv2.add(x,y))#[[255]],260->255
print(x+y)#[4],260%256=4

'''
图像混合
这其实也是加法，但是不同的是两幅图像的权重不同，这就会给人一种混
合或者透明的感觉。
g (x) = (1 − α) f0 (x) + αf1 (x)
函数 cv2.addWeighted() 可以按下面的公式对图片进行混合操作
dst = α · img1 + β · img2 + γ

请牢记，如果图片大小也就是水平和竖直方向上的像素数量不同，就会报错的。
我们可以在画图软件中调整一下图片大小。
'''
img1=cv2.imread('pic/wechat.png')
img2=cv2.imread('pic/mongodb.jpg')

dst=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imwrite('pic/10-1-1.jpg',dst)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()