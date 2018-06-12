import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#计算均值的自定义函数
#传入数据为numpy格式的矩阵，行表示样本数，列表示特征
def UserMean(dataX):
    #axis=0,表示按照列来求均值
    #如果传入的参数是list，则axis=1
    return np.mean(dataX,axis=0)

def UserPCA(Xmat,k):
    average=UserMean(Xmat)
    m,n=np.shape(Xmat)
    data_adjust=[]
    avgs=np.tile(average,(m,1))
