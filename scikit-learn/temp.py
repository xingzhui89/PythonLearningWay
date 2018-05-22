from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

cmap=colors.LinearSegmentedColormap(
    'red_blue_classes',
    {
        'red':[(0,1,1),(1,0.7,0.7)],
        'green':[(0,0.7,0.7),(1,0.7,0.7)],
        'blue':[(0,0.7,0.7),(1,1,1)]
    }
)
plt.cm.register_cmap(cmap=cmap)

def dataset_fixed_cov():
    n,dim=300,2
    np.random.seed(0)
    C=np.array([[0.,-0.23],[0.83,.23]])
    X=np.r_[np.dot(np.random.randn(n,dim),C),np.dot(np.random.randn(n,dim),C)+np.array([1,1])]
    y=np.hstack((np.zeros(n),np.ones(n)))
    return X,y

def dataset_cov():
    '''Generate 2 Gaussians samples with different covariance matrices'''
    n, dim = 300, 2
    np.random.seed(0)
    C = np.array([[0., -1.], [2.5, .7]]) * 2.
    X = np.r_[np.dot(np.random.randn(n, dim), C),
              np.dot(np.random.randn(n, dim), C.T) + np.array([1, 4])]
    y = np.hstack((np.zeros(n), np.ones(n)))
    return X, y





plt.show()