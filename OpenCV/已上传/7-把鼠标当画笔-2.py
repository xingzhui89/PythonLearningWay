'''
这个案例，我们要实现的功能是在拖动鼠标时绘制矩形或者圆圈。
所以我们要设置两个过程，一个是画矩形，一个是画圆圈。

'''
import cv2
import numpy as np

#表示是否可以进行绘制，当鼠标按下时为True
drawing=False
#绘制圆圈还是绘制矩形的控制变量，通过键盘m键来控制切换
mode=True
#ix,iy表示初始位置
ix,iy=-1,-1


img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')

def draw_cirlce(event,x,y,flags,param):
    # 表示可以在函数中修改全局变量的值
    global ix,iy,drawing,mode
    #如果是左键单击
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),1,(0,0,255),-1)
    #如果鼠标左键抬起，那么就停止绘图
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
    #如果没有这个判断，会出现一些错误
    else:
        return

cv2.setMouseCallback('image',draw_cirlce)

while(True):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k==ord('m'):
        mode=not mode
    elif k==27:
        break

'''
通过实践，这个程序还存在一点问题
1、矩形的实心的，图形会覆盖
2、绘制圆圈时，如果鼠标移动速度不同，那么圆圈之间的距离也是在变化的。

所以如何控制绘图频次或者程序接收光标坐标的频次。
'''