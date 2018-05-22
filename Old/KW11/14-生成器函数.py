# 第一个测试
import time
def generator():
	print('开始生孩子啦。。。。。。')
	print('开始生孩子啦。。。。。。')
	print('开始生孩子啦。。。。。。')
	yield '我' #yield是生成器的关键，遇到yield就是抛出后面的内容，跳出函数体，再次运行这个函数时，从yield之后开始运行

	time.sleep(3)
	print('开始生儿子啦')
	yield '儿子'

	time.sleep(3)
	print('开始生孙子啦')
	yield '孙子'

res=generator()
print(res)
print(res.__next__()) #这时开始运行生儿子的代码
print(res.__next__()) #这时开始运行生孙子的代码
print(res.__next__()) #结束了


#第二个测试
#这个函数直接把所有的包子都生成到list中了
def product_baozi():
	ret=[]
	for i in range(100):
		ret.append('一屉包子%s' %i)
	return ret
baozi_list=product_baozi()
print(baozi_list)

#这个函数是一个一个的生产，不是一次性的
def product_baozi():
	for i in range(100):
		print('正在生产包子')
		yield '一屉包子%s' %i #i=1
		print('开始卖包子')
pro_g=product_baozi()

print(pro_g)
print(pro_g.__next__())
print(pro_g.__next__())
baozi1=pro_g.__next__()
#加代码
baozi1=pro_g.__next__()


def xiadan():
	ret=[]
	for i in range(10000):
		ret.append('鸡蛋%s' %i)
	return ret

print(xiadan())
#缺点1：占空间大
#缺点2：效率低

def xiadan():
	for i in range(5):
		yield '鸡蛋%s' %i

alex_lmj=xiadan()
print(alex_lmj.__next__())
print(alex_lmj.__next__())
print(alex_lmj.__next__())
print(alex_lmj.__next__())
print(alex_lmj.__next__())
print(alex_lmj.__next__())

# 如果不想一个个的打印，可以通过循环来实现
for jidan in alex_lmj:
	print(jidan)


jidan=alex_lmj.__next__()
jidan=alex_lmj.__next__()
jidan=alex_lmj.__next__()
jidan=alex_lmj.__next__()
jidan=alex_lmj.__next__()
jidan=alex_lmj.__next__()

print('zhoushaochen 取鸡蛋',jidan)