'''
1、模板匹配的原理
    模板匹配用来在一副大图中搜寻查找模板图像位置的方法。
    OpenCV提供了函数：matchTemplate()。
    和2D卷积一样，也是用模板图像在输入图像上滑动，并在每一个位置对模板图像和与其对应的输入图像的子区域进行比较。
    返回的结果是一个灰度图像，每一个像素值表示此区域与模板的匹配程度。
    如果输入图像的大小是WxH,模板的大小是wxh，输出结果为(W-w+1,H-h+1)。
    得到结果后，就使用函数minMaxLoc()来获取其中最大值和最小值的位置。
'''

'''
2、OpenCV中的模板匹配
    我们还是以梅西的头像为例，先做一个模板出来，只包含他的头部。。。
    然后我们尝试不同的比较方法。
    请看代码：
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img=cv2.imread('pic/messi.jpg',0)
# img2=img.copy()
# template=cv2.imread('pic/messi_face.jpg',0)
# w,h=template.shape[::-1]#w是水平，h是竖直方向
# #print(w,h)
# methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR',
#          'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']
# for meth in methods:
#     img=img2.copy()
#     method=eval(meth)
#     res=cv2.matchTemplate(img,template,method)
#     min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
#     if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
#         top_left=min_loc
#     else:
#         top_left=max_loc
#     bottom_right=(top_left[0]+w,top_left[1]+h)
#     cv2.rectangle(img,top_left,bottom_right,255,2)
#
#     plt.subplot(121), plt.imshow(res, cmap='gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122), plt.imshow(img, cmap='gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#     plt.show()
###此处插入图片24-1
'''
    运行上述代码，可以依次看到采用不同方法获取到的结果。
    
3、多对象的模板匹配
    在上面的案例中，梅西只在图片中出现了一次。
    假设我们的目标对象在图片中出现多次怎么办？
    minMaxLoc()只会给出最大值和最小值。所以我们要借助阈值。
    我们在经典游戏《超级玛丽》中找一个金币图。
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb=cv2.imread('pic/mario.jpg')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template=cv2.imread('pic/mario_coin.jpg',0)
w,h=template.shape[::-1]

res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.8

loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imwrite('pic/24-2.jpg',img_rgb)
###此处插入图片24-2