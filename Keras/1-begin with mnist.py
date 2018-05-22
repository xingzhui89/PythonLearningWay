from keras.models import Sequential
from keras.layers.core import Dense
from keras.datasets import mnist
from keras.utils import np_utils
from keras.optimizers import SGD,RMSprop,Adam,Adagrad

def load_data():
    (x_train,y_train),(x_test,y_test)=mnist.load_data()
    number=55000
    x_train=x_train[0:number]
    y_train=y_train[0:number]
    x_train=x_train.reshape(number,28*28).astype('float32')
    x_test=x_test.reshape(x_test.shape[0],28*28).astype('float32')
    x_train/=255
    x_test/=255

    y_train=np_utils.to_categorical(y_train,10)
    y_test=np_utils.to_categorical(y_test,10)

    return (x_train,y_train),(x_test,y_test)

batch_size=100
np_epoch=10

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("mnist/", one_hot=True)

X_train, Y_train = mnist.train.images,mnist.train.labels
X_test, Y_test = mnist.test.images, mnist.test.labels

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
print(X_train.shape,X_test.shape,Y_train.shape,Y_test.shape)

X_train/=255
X_test/=255
print(X_train.shape[0],'train samples')
print(X_test.shape[0],'test samples')

model=Sequential()
model.add(Dense(input_dim=28*28,units=500,activation='relu'))

model.add(Dense(units=500,activation='relu'))

# model.add(Dense(units=500,activation='tanh'))

model.add(Dense(output_dim=10,activation='softmax'))

model.summary()

model.compile(optimizer=RMSprop(),loss='categorical_crossentropy'
              ,metrics=['accuracy'])
'''
b=100,np=10,relu的情况下得到如下结果：
使用RMSprop，acc:96.85%
Adam,acc:96.61%
SGD,acc:11.35%(默认参数)
Adagrad,acc:91.84%

RMSprop,np=10,relu:
bs=10,acc:97.1%
bs=100,acc:96.85%
bs=1000,acc:90,64%
bs=10000,acc:67.43%

RMSprop,bs=100,relu:
np=10,acc=96.85%
'''
# model.compile(optimizer=SGD(lr=0.01),loss='mse'
#               ,metrics=['accuracy'])

history=model.fit(X_train,Y_train,batch_size=batch_size,epochs=np_epoch)

score=model.evaluate(X_test,Y_test)
print('Test score:',score[0])
print('Test accuracy:',score[1])

# result=model.predict(x_test)


