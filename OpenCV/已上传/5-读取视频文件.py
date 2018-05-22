'''
视频的读取
与从摄像头中捕获一样，你只需要把设备索引号改成视频文件的名字。在
播放每一帧时，使用 cv2.waiKey() 设置适当的持续时间。如果设置的太低视
频就会播放的非常快，如果设置的太高就会播放的很慢（你可以使用这种方法
控制视频的播放速度）。通常情况下 25 毫秒就可以了
'''
import cv2

cap=cv2.VideoCapture('pic/output.avi')

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret:
        #frame=cv2.flip(frame,0)
        cv2.imshow('frame',frame)
    else:
        break
    if cv2.waitKey(100)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()