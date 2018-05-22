'''
学习使用OpenCV绘制不同几何图形
学习的函数包括：；
cv2.line()用来绘制直线
cv2.circle()用来绘制圆
cv2.rectangle()用来绘制矩形
cv2.ellipse()用来绘制椭圆
cv2.putText()用来输出文字
上面几个函数，都需要设置一下参数：
• img：你想要绘制图形的那幅图像。
• color：形状的颜色。以 RGB 为例，需要传入一个元组，例如：（255,0,0）
代表蓝色。对于灰度图只需要传入灰度值。
• thickness：线条的粗细。如果给一个闭合图形设置为 -1，那么这个图形
就会被填充。默认值是 1.
• linetype：线条的类型， 8连接，抗锯齿等。默认情况是 8连接。 cv2.LINE_AA
为抗锯齿，这样看起来会非常平滑。
'''

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),5,cv2.LINE_AA)
cv2.rectangle(img,(384,15),(500,228),(0,255,0),3)
cv2.circle(img,(447,63),63,(0,0,255),-1)
cv2.ellipse(img,(256,256),(100,50),-45,0,180,255,-1)
cv2.putText(img,'OpenCV',(10,500),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
