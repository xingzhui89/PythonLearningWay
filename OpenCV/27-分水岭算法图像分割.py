'''
使用分水岭Watershed算法基于掩膜mask进行图像分割
使用的函数为cv2.watershed()

原理
    任何一副灰度图像都可以被看成拓扑平面，灰度高的区域看成山峰，灰度低的区域看成山谷。
    我们向每一个山谷中灌不同颜色的水。随着水位的升高，不同山谷中的水就会汇合。
    为了防止不同山谷的水汇合，需要在汇合的地方构建堤坝。
    最终我们构建的堤坝就是对图像的分割。
    为了防止过度分割，OpenCV采用基于mask的分水岭算法。
    我们要设置哪些山谷点会汇合，哪些不会。这是一种交互式的图像分割。
    我们需要将已知的对象打上不同的标签。
    如果某个区域肯定是前景或者对象，我们用某个颜色标签标记它。
    如果某个区域肯定是背景，我们用另外一种颜色来标记。
    剩下不确定的区域用0来标记。
    然后实施分水岭算法，每一次灌水，标签更新一次。
    当两个不同颜色的标签相遇时，就构建堤坝，直到将所有山峰淹没，最后得到我们的边界对象的值为-1.

    我们来看个例子：将一堆紧挨在一起的硬币进行分割。
    如果我们使用阈值操作，仍然得到紧挨在一起的结果。
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic/coins.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# plt.subplot(121),plt.imshow(gray),plt.title('Gray')
# plt.subplot(122),plt.imshow(thresh),plt.title('Thresh')
# plt.show()
#插入图片27-1，Gray和Thresh的对比
'''
    现在我们向去除图像中的所有的白噪声，需要使用形态学中的开运算。
    去除对象上小的空洞，我们需要使用形态学闭运算。
    靠近对象中心的区域肯定是前景，远离对象中心的区域肯定是背景。
    不确定的区域就是硬币之间的边界。
    我们要提取的肯定是硬币的区域。
    腐蚀操作可以去除边缘像素，但是由于硬币接触，这种操作失效。
    另外一个选择就是距离变换加上合适的阈值，进行膨胀操作。
    膨胀可以将对象的边界延伸到背景中，由于边界区域被去处理，我们就直到哪些区域肯定是前景，哪些肯定是背景。
    从肯定不是背景的区域中减去肯定是前景的区域就得到了边界区域。
'''
kernal=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernal,iterations=2)

sure_bg=cv2.dilate(opening,kernal,iterations=3)

dist_transform=cv2.distanceTransform(opening,1,5)
ret,sure_fg=cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

sure_fg=np.uint8(sure_fg)
unknown=cv2.subtract(sure_bg,sure_fg)

# plt.subplot(121),plt.imshow(dist_transform),plt.title('dist_transform')
# plt.subplot(122),plt.imshow(sure_fg),plt.title('sure_fg')
# plt.show()
#插入图片27-2

'''
    这样，我们直到哪些是背景哪些是硬币了。
    然后创建标签，并标记其中的区域。。
    利用cv2.connectedComponents()函数来完成这个事情。
    背景标记为0，其他对象从1开始标记。
'''

ret,markers1=cv2.connectedComponents(sure_fg)
markers=markers1+1
markers[unknown==255]=0

markers3=cv2.watershed(img,markers)
img[markers3==-1]=[255,0,0]
plt.subplot(121),plt.imshow(markers1),plt.title('markers1')
plt.subplot(122),plt.imshow(img),plt.title('img')
plt.show()
#插入图27-3