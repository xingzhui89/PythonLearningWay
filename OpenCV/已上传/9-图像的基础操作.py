'''
我们的目标是：
1、获取像素值并修改
2、获取图像的属性和信息
3、图像的ROI()
4、图像通道的拆分及合并
这些操作都需要用到Numpy，因为涉及到矩阵操作，比使用纯python代码要高效很多。
'''

import cv2
import numpy as np

img=cv2.imread('pic/mongodb.jpg')
#这是为了获取img的大小
print(np.shape(img))#(450, 600, 3)
#如果是img的两维定位的是像素点，
px=img[100,100]
print(px)#[255 255 255]
white=img[100,100,0]#第三个维度就是rgb中的颜色
print(white)#255

#矩阵操作，把x和y方向上的前100个像素点都设置同一个颜色
img[:100,:100]=[100,176,30]
print(img[50,50,0])#b,100
print(img[50,50,1])#g,176
print(img[50,50,2])#r,30

'''
上面提到的方法被用来选取矩阵的一个区域，比如说前 5 行的后 3
列。对于获取每一个像素值，也许使用 Numpy 的 array.item() 和 array.itemset() 会更好。但是返回值是标量。如果你想获得所有 B， G， R 的
值，你需要使用 array.item() 分割他们。
'''
print(img.item(10,10,2))
img.itemset((10,10,2),100)

'''
img.shape 可以获取图像的形状。他的返回值是一个包含行数，列数，通道数的元组。
img.size 可以返回图像的像素数目
img.dtype 返回的是图像的数据类型
'''
print(img.shape)
print(img.size)
print(img.dtype)

'''
下面的操作会将前面一个区域中的图像，复制到后面一个区域
'''
leaf=img[150:300,0:100]
img[150:300,100:200]=leaf

'''
如果你想在图像周围创建一个边，就像相框一样，你可以使用 cv2.copyMakeBorder()
函数。这经常在卷积运算或 0 填充时被用到。
这个函数的参数包括：
• src 输入图像
• top, bottom, left, right 对应边界的像素数目。
• borderType 要添加那种类型的边界
    - cv2.BORDER_CONSTANT 添加有颜色的常数值边界，还需要
    下一个参数（values）。
    – cv2.BORDER_REFLECT 边界元素的镜像。比如: fedcba|abcdefgh|hgfedcb
    – cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT
    跟上面一样，但稍作改动。例如: gfedcb|abcdefgh|gfedcba
    – cv2.BORDER_REPLICATE 重复最后一个元素。
'''

img=cv2.copyMakeBorder(img,50,50,50,50,borderType=cv2.BORDER_REFLECT)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
OpenCV中是按照BGR排列
Matplotlib中按照RGB排列通道
'''