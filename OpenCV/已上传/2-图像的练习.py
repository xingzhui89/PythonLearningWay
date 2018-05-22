'''
接下来，我们尝试一个加载一个灰度图片，显示该图片，当检测到按下s键时保存并退出
或者按下ESC键时退出不保存。
'''

import numpy as np
import cv2

img=cv2.imread('pic/mongodb.jpg',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('pic/mongodb_test.png',img)
    cv2.destroyAllWindows()