import numpy as np
from sklearn.svm import SVC

rng=np.random.RandomState(0)
X=rng.rand(100,10)
y=rng.binomial(1,0.5,100)
X_test=rng.rand(5,10)

clf=SVC()
s1=clf.set_params(kernel='linear').fit(X,y)
r1=clf.predict(X_test)
print(r1)
# [1 0 1 1 0]

s2=clf.set_params(kernel='rbf').fit(X,y)
r2=clf.predict(X_test)
print(r2)
# [0 0 0 1 0]


