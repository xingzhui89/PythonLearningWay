#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n
		
# for g in _odd_iter():
	# if g<100:
		# print(g)
	# else:
		# break

def _not_divisible(n):
	return lambda x:x%n>0
#返回的是一个函数，这个函数的返回值是true或false

def primes():
	yield 2
	it=_odd_iter()
	#建立所有的奇数序列，因为素数是除2之外都是奇数
	while True:
		n=next(it)
		yield n
		it=filter(_not_divisible(n),it)
		#重新建立一个序列，把能被n整除的都筛选掉，只保留不能被n整除的数字。

for n in primes():
	if n<100:
		print(n)
	else:
		break

		
def _rev(s):
	return s[::-1]#将字符串逆序排列的很好的办法，或者直接采用reverse（）方法
def is_palindrome(n):
	s=str(n)
	a=_rev(s)
	return s==a
output = filter(is_palindrome, range(10, 1000))
print(list(output))