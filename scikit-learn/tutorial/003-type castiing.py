from sklearn import datasets
from sklearn.svm import SVC

iris=datasets.load_iris()
# print(iris.keys())
# print(iris['target_names'])
# print(iris['feature_names'])

clf=SVC()
f1=clf.fit(iris['data'],iris['target'])
print(f1)
'''
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
'''
print(list(clf.predict(iris['data'][:3])))
# [0, 0, 0]

f2=clf.fit(iris['data'],iris['target_names'][iris['target']])
print(f2)
'''
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
'''
print(list(clf.predict(iris['data'][:3])))
# ['setosa', 'setosa', 'setosa']


