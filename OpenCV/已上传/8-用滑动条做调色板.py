'''
本例介绍如何讲滑动条绑定到opencv的窗口
def getTrackbarPos(trackbarname, winname)
def createTrackbar(trackbarName, windowName, value, count, onChange)
函数的一个参数是滑动条的名字，
第二个参数是滑动条被放置窗口的名字，
第三个参数是滑动条的默认位置。
第四个参数是滑动条的最大值，
第五个函数是回调函数，每次滑动条的滑动都会调用回调函数。回调函数通常都会含有一个默认参数，就是滑动条的位置。
'''

import cv2
import numpy as np

#这里我们不定义操作，简单一些
def nothing(x):
    pass

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(True):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k==27:
        break
    #通过getTrackbarPos获取指定的值
    r=cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s==0:
        img[:]=0
    else:
        #这句代码的含义是，img中的每个像素点都定义成[b,g,r]
        img[:]=[b,g,r]

cv2.destroyAllWindows()