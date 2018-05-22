'''
学习如何在一张图片中检测直线
主要涉及的函数包括cv2.HoughLines(),cv2.HoughLinesP()

原理
    霍夫变换在检测各种形状的技术中非常流行。
    如果我们要检测的形状可以用数学表达式写出，那么就可以利用霍夫变换。
    即使要检测的形状存在一点破环或者扭曲也可以使用。
    我们以检测直线为例介绍。
   ？这里还需要进一步的介绍，上传的时候补上，先把原理搞明白
'''

'''
2、OpenCV中的霍夫变换
    OpenCV中封装了一个cv2.HoughLines()函数。
    def HoughLines(image, rho, theta, threshold, lines=None, srn=None, stn=None, min_theta=None, max_theta=None)
    返回值为(ρ,θ)，其中ρ单位是像素，θ单位是弧度。
    这个函数的第一个参数是一个二值化图像，所以进行霍夫变换时首先要进行二值化。
    第二个和第三个值分别代表ρ和θ的精确度。
    第四个参数是阈值，只有累加其中的值高于阈值时才被认为是一条直线。
    也可以看作能检测到的直线的最短长度。
    
'''
# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv.imread('pic/sudoku.jpg')
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# edges=cv.Canny(gray,50,150,apertureSize=3)
#
# lines=cv.HoughLines(edges,1,np.pi/180,200)
# #print(lines)
# for line in lines:
#     #print(line)
#     rho,theta=line[0]
#     a=np.cos(theta)
#     b=np.sin(theta)
#     x0=a*rho
#     y0=b*rho
#     x1=int(x0+1000*(-b))
#     y1=int(y0+1000*(a))
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * (a))
#     cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#
# plt.subplot(121), plt.imshow(edges)
# plt.subplot(122), plt.imshow(img)
# plt.show()
# cv.imwrite('pic/25-1-houghlines.jpg',img)
# #插入图片25-1
# #插入图片25-2

'''
3、Probabilistic Hough Transform
    通过上面的讲解，我们知道每一条直线都需要两个参数，计算量比较大。
    PHT是对霍夫变换的一种优化，不会对每个点进行计算，而是从图像中随机选取一个点集进行计算。
    但是我们需要降低阈值。
    通过使用cv2.HoughLinesP()函数来实现这个算法。
    第一个参数是minLineLength--线的最短长度，比这个短的线会被忽略。
    第二个参数MaxLineGap--两条线段之间的最大间隔，小于此值，认为是一条直线。
    这个函数返回的是直线的起点和终点。
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic/sudoku.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150,apertureSize=3)
minLineLength=100
maxLineGap=10
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
plt.subplot(121), plt.imshow(edges)
plt.subplot(122), plt.imshow(img)
plt.show()
cv2.imwrite('pic/25-3.jpg',img)
