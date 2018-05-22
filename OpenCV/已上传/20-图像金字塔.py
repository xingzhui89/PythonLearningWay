'''
图像金字塔
一般情况，我们要处理一副具有固定分辨率的图像。
但是有些情况，我们需要对同一图像的不同分辨率的子图像进行处理。
比如我们要在某个图像中查找某个目标，比如一张脸，但是我们不知道目标在图像中的尺寸大小。
这时候我们需要创建一组图片，具有不同的分辨率，然后在所有的图片中搜索目标。
这些具有不同分辨率的图像被成为图像金字塔Image Pyramids。
其中高层的图片具有较低的分辨率，底层的图片具有较高的分辨率。

一般我们使用两种图像金字塔，高斯金字塔和拉普拉斯金字塔。

高斯金字塔的原理：
    高层图片是通过将底部图像中的连续的行和列去除而得到的。
    高层图片中的每个像素值等于下一层图像中的5个像素的高斯加权平均值。
    这样操作一次，一张MxN大小的图像，就会变成一个M/2xN/2的图像，面积变为原来的1/4.
    连续操作就可以得到分辨率不断下降的图像金字塔。
    函数pyrDown()从一个高分辨率大尺寸的图像向上构建一个金字塔。
    函数pyrUp()，从一个低分辨率小尺寸的图像向下构建一个金字塔。

这里的up还有down指的是分辨率上的改变。
'''
# import cv2
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg')
# lower_reso=cv2.pyrDown(img)
# higher_reso2 = cv2.pyrUp(lower_reso)
# plt.subplot(131),plt.imshow(img),plt.title('IMG')
# plt.subplot(132),plt.imshow(lower_reso),plt.title('LOWER_RESO')
# plt.subplot(133),plt.imshow(higher_reso2),plt.title('higher_reso2')
# plt.show()

# cv2.imshow('messi',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
'''
但是将图片的分辨率降低之后，会丢失很多信息，再通过pyrUp方法提升分辨率，得到的也不是原来的图片。

拉普拉斯金字塔可以由高斯金字塔计算而来。
其图像看起来像是边界图，大部分元素都是0.常被用来图像压缩。
通过求解高斯金字塔某一层与其低一层的图像的差subtract来获取。

'''
'''
图像金字塔主要应用于图像融合。
例如，在图像缝合中，需要将两幅图像叠加在一起，但是由于链接区域图像像素的不连续性，整幅图像的效果会很差。
我们通过一个实例来展示如何无缝融合两个图像。
我们要实现将一个苹果和一个橘子融合到一起。
具体步骤如下：
1、读取两幅图像，苹果和橘子
2、构建苹果和橘子的高斯金字塔，6层。
3、根据高斯金字塔计算拉普拉斯金字塔。
4、在拉普拉斯的每一层进行图像融合。
5、根据融合后的图像金字塔重建原始图像。

下面是实现代码：
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#读入两张图片
A=cv.imread('pic/apple.jpg')
A=cv.cvtColor(A,cv.COLOR_BGR2RGB)
B=cv.imread('pic/orange.jpg')
B=cv.cvtColor(B,cv.COLOR_BGR2RGB)


#print(dir(A))
G=A.copy()#copy命令并没有直接弹出来，不知道是那个类的方法.但是通过dir命令，真的发现由copy方法。
gpA=[G]#gpA用于存储A的高斯金字塔图像
for i in range(6):#连续六次使用高斯金字塔运算
    G=cv.pyrDown(G)#使分辨率下降
    gpA.append(G)
print('gpA中含有 %d 个元素'% len(gpA))

G=B.copy()
gpB=[G]
for i in range(6):#0,1,2,3,4,5
    G=cv.pyrDown(G)
    gpB.append(G)
print('gpB中含有 %d 个元素'% len(gpB))

lpA=[gpA[5]]
for i in range(5,0,-1):#5,4,3,2,1
    GE=cv.pyrUp(gpA[i])#尺寸上与gpA[i-1]是相同的，但是内容肯定有缺失
    #print(GE.shape)
    #print(gpA[i-1].shape)
    L=cv.subtract(gpA[i-1],GE)#这句话是求拉普拉斯图像的方法。
####很重要的一点，两张图片的像素数要保持一致，并且应该是2的6次方的倍数，否则会出现错误。
    lpA.append(L)

lpB=[gpB[5]]
for i in range(5,0,-1):#5,4,3,2,1
    GE=cv.pyrUp(gpB[i])
    L=cv.subtract(gpB[i-1],GE)
    lpB.append(L)

LS=[]
for la,lb in zip(lpA,lpB):
    rows,cols,dpt=la.shape
    print('rows:{0},cols:{1},dpt:{2}'.format(rows,cols,dpt))
    x=int(cols/2)
    ls=np.hstack((la[:,0:x],lb[:,x:]))
    LS.append(ls)

ls_=LS[0]
for i in range(1,6):
    ls_=cv.pyrUp(ls_)
    ls_=cv.add(ls_,LS[i])

arow,acols,ach=A.shape
a=int(acols/2)
real=np.hstack((A[:,:a],B[:,a:]))

plt.subplot(121),plt.imshow(ls_),plt.title('Pyramid_blending')
plt.subplot(122),plt.imshow(real),plt.title('Direct_blending')
plt.show()



