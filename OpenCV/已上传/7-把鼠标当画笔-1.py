'''
学习使用OpenCV处理鼠标事件
涉及到的函数是cv2.setMouseCallBack()

第一个例子，我们创建一个简单的程序，在我们双击过的地方绘制一个圆。
首先我们来创建一个鼠标事件回调函数，但鼠标事件发生是他就会被执行。
鼠标事件可以是鼠标上的任何动作，比如左键按下，左键松开，左键双击等。
我们可以通过鼠标事件获得与鼠标对应的图片上的坐标。根据这些信息我们可
以做任何我们想做的事。
'''

import cv2
import numpy as np

# events=[i for i in dir(cv2) if 'EVENT' in i]
# print(events)
#首先要创建图像，也就是一个画布
img=np.zeros((512,512,3),np.uint8)
#这里的shape是3个参数的，没搞懂，按理说是三维的数组
#print(img)
cv2.namedWindow('image')

#定义双击的具体实现函数，用于后面与双击事件的绑定
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
cv2.setMouseCallback('image',draw_circle)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(20)==27:#模拟ESC按键
        break

cv2.destroyAllWindows()