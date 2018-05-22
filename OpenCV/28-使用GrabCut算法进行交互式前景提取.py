'''
原理：
在提取前景的操作中需要尽可能少的人机交互，GrabCut算法十分合适。
它的工作方式是这样的，开始时用户用一个矩形将前景区域框住，然后算法进行迭代式分割直到最好结果。
有时候分割的结果会把前景和背景搞混，这时候需要用户来修正一下，就是在对应位置点一下即可。
我们再来详细的解释一下，
·输入的矩形，外部肯定都是背景，但是内部是未知的。
·计算机会对我们输入的图像做一个初始化标记，标记前景和背景像素。
·使用一个高斯混合模型GMM对前景和背景建模。
·根据输入，GMM会学习并创建心的像素分布。对于未知的像素，根据其与已知分类的像素的关系来进行分类。
·这样就会根据像素的分布创建一副图，图中的节点就是像素点。除了像素点还有两个节点Source_node和Sink_node。
    所有的前景像素都和Source_node相连，背景像素与Sink_node相连。
·将像素连接到Source_node/end_node的权重由它们属于同一类的概率来决定。
    两个像素之间的权重由边的信息或者两个像素的相似性来决定。
    如果两个像素的颜色有很大的不同，那么它们之间边的权重就会很小。
·使用mincut算法对上面得到的图进行分割。它会根据最低成本方程将图分为Source_node和Sink_node。
    成本方程就i是被剪掉的所有边的权重之和。
    在裁剪之后，所有连接到Source_node的像素被认为是前景，链接到Sink_node的像素被认为是背景。
·继续这个过程直到分类收敛。


实例演示：
OpenCV中提供了函数grabCut()。参数包括：
·img-输入图像
·mask-掩膜图像，用来确定哪些区域是背景，前景或者前景/背景等。
    可以设置为GC_BGD,GC_FGD,GCPR_BGD,GC_PR_FGD等，或者直接输入0，1，2，3
·rect-包含前景的矩形，格式为(x,y,w,h)
·bgdModel，fgdModel-算法内部使用的数组，只需要创建两个大小为(1,65)数据类型为float64的数组。
·iterCount-算法的迭代次数。
·mode可以设置为GC_INIT_WITH_RECT或者GC_INIT_WITH_MASK,或者联合使用。

首先我们来看使用矩形模式。
加载图片，创建掩膜图像，构建bgdModel和fgdMode。
传入矩形参数，让算法迭代5次。
由于我们在使用举行模式所以修改模式设置为GC_INIT_WITH_RECT。
运行grabCut，算法会修改掩膜图像。
在新的掩膜图像中，所有的像素被分为4类，背景，前景，可能是背景/前景，使用4个不同的标签标记。
然后我们来修改掩膜图像，所有的0和1元素都归为0背景，所有的1和3像素都归为1前景。


'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('pic/messi1.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
mask=np.zeros(img.shape[:2],np.uint8)

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)

rect=(230,60,600,600)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]

plt.imshow(img),plt.colorbar()
plt.show()
#插入图片，28-1

'''
这次提取的效果不是很好，背景中有些色彩没有去除。
如果想要得到比较精确的结果，那么就要修改掩膜图像才可以。
因为我们交互上的缺陷，所以只能重建一个图片，作为新的掩膜图像。
用图像编辑软件打开输入图像，在前景处用白色绘制，在背景上用黑色绘制。
其他地方用灰色填充，保存成新的掩膜。
新添加的代码如下：
'''

newmask=cv2.imread('pic/messi_mask.jpg',0)
mask[newmask==0]=0
mask[newmask==255]=1



