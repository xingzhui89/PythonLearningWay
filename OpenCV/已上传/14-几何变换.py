'''
如果对图像进行各种几何变换，比如移动，旋转，仿射变换等。
主要涉及的函数中cv2.getPerspectiveTransform
OpenCV中哦提供了两个变换函数，cv2.warpAffine和cv2.warpPerspective。
warpAffine接收的参数是2x3的变换矩阵
warpPerspective接收的参数是3x3的变换矩阵
'''

'''
一、扩展缩放，只改变图像的尺寸大小。
OpenCV提供的函数cv2.resize()可以实现这个功能。
def resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None):
通过手动设置图像的尺寸，或者指定缩放因子。
这里还需要设置插值方法，在缩小时使用cv2.INTER_AREA
在扩大时使用cv2.INTER_CUBIC和cv2.INTER_LINEAR。
举个例子
'''

# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/mongodb.jpg')
# #这是通过设置缩放系数来实现
# res=cv.resize(img,None,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
#
# #这是通过直接设置图像尺寸来控制大小
# height,width=img.shape[:2]
# #res=cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)
#
# plt.subplot(121),plt.imshow(img),plt.title('Input'),plt.xticks([0,1000]),plt.yticks([0,200])
# plt.subplot(122),plt.imshow(res),plt.title('Output'),plt.xticks([0,1000]),plt.yticks([0,200])
# plt.show()


'''
二、平移就是将对象换一个位置。
如果要沿(x,y)方向平移，移动的距离是(tx,ty)，那么构建的移动矩阵位：
M=[[1,0,tx],[0,1,ty]]
我们可以通过Numpy来构建这个矩阵，然后传递给cv2.warpAffine()。
举个实例
'''
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt
#
# img = cv.imread('pic/mongodb.jpg',0)
# rows,cols = img.shape
#
# '''
# #def warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None):
# '''
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv.warpAffine(img,M,(cols,rows))
#
# plt.subplot(121),plt.imshow(img),plt.title('Input'),plt.xticks([0,1000]),plt.yticks([0,200])
# plt.subplot(122),plt.imshow(dst),plt.title('Output'),plt.xticks([0,1000]),plt.yticks([0,200])
# plt.show()
'''
三、旋转
对一个图像旋转角度θ，需要用到下面的旋转矩阵
M=[[cosθ,-sinθ],[sinθ,cosθ]]
OpenCV允许在任意地方进行旋转,但是旋转矩阵的形式应该修改成一个比较复杂的格式:
这里就不展开介绍了.
我们可以利用函数cv2.getRotationMatrix2D来构建这个矩阵。
举个实例：
'''

# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/mongodb.jpg',0)
# rows,cols=img.shape
#
# M=cv.getRotationMatrix2D((cols/2,rows/2),45,0.6)
#
# dst=cv.warpAffine(img,M,(2*cols,2*rows))
# # while(1):
# #     cv.imshow('img',dst)
# #     if cv.waitKey(1)==27:
# #         break
# # cv.destroyAllWindows()
# plt.subplot(121),plt.imshow(img),plt.title('Input'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Output'),plt.xticks([]),plt.yticks([])
# plt.show()

'''
四、仿射变换
在仿射变换中，原图中所有的平行线在结果图像中同样平行。
为了创建这个矩阵，我们需要从原图中找到三个点以及他们在输出图像中的位置。
然后cv2.getAffineTransform会创建一个2x3的矩阵，最后这个矩阵传递给
cv2.warpAffine函数。
'''

# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/affine.jpg')
# rows,cols,chs=img.shape
#
# pts1=np.float32([[50,50],[200,50],[50,200]])
# pts2=np.float32([[10,100],[200,50],[100,250]])
#
# M=cv.getAffineTransform(pts1,pts2)
# dst=cv.warpAffine(img,M,(cols,rows))
#
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()


'''
五、透视变换
对于视角变换，我们需要3x3的矩阵，变换前后不改变直线。
要构建这个变换矩阵，需要在输入图像上找到4个点，以及他们在输出图上的位置。
这四个点中的任意三点都不能共线。
同样的，我们可以利用cv2.getPerspectiveTransform()构建变换矩阵。
然后传递给cv2.warpPerspective
看个实例：
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic/perspective.jpg')
rows,cols,chs=img.shape

pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])

M=cv.getPerspectiveTransform(pts1,pts2)

dst=cv.warpPerspective(img,M,(300,300))

plt.subplot(122),plt.imshow(img),plt.title('Input')
plt.subplot(121),plt.imshow(dst),plt.title('Output')
plt.show()