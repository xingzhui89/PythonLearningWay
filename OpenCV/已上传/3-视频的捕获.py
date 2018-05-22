'''
今天主要讲一下如何读取视频文件，显示视频，保存视频文件
学会从摄像头获取并显示视频
cv2.VideoCapture(),cv2.VideoWrite()是今天主要使用的函数
'''

'''
1、捕获视频
简单的任务是从摄像头捕获一段视频，并把它转换成灰度视频显示出来。
为了获取视频，你应该创建一个 VideoCapture 对象。
他的参数可以是设备的索引号，或者是一个视频文件。
设备索引号就是在指定要使用的摄像头。
一般的笔记本电脑都有内置摄像头。所以参数就是 0。
你可以通过设置成 1 或者其他的来选择别的摄像头。
之后，你就可以一帧一帧的捕获视频了。但是最后，别忘了停止捕获视频。
cap.read()返回一个布尔值，如果帧读取的是正确的，就是True，所以通过检查该函数的返回值来确定视频文件是否已经到了结尾。

可以使用函数 cap.get(propId) 来获得视频的一些参数信息，比如我们要获取每一帧的宽和高。
其实这个是比较固定的。
'''
import cv2

cap=cv2.VideoCapture(0)
i=0
while(True):
    i=i+1
    ret,frame=cap.read()
    print('Frame ID: ',i,cap.get(3),cap.get(4))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()