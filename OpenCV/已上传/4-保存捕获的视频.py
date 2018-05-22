'''
保存视频的操作
需要创建一个VideoWriter的对象，我们应该确定一个输出文件的名字。
指定FourCC编码，播放帧率和帧的大小也需要确定，最后就是isColor标签。

在下面的例子中
首先通过VideoCapture函数得到一个抓取器
FOURCC的设置方法，在opencv3中也有所改变
然后定义了一个VideoWriter对象。
'''
import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter('pic/output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    #这里的ret值得是read方法的结果，如果读到帧，就是true，否则就是false
    ret,frame=cap.read()
    if ret==True:
        #frame=cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        cap.open()

cap.release()
out.release()
cv2.destroyAllWindows()
