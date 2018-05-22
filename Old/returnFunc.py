#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum
	
#我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f=lazy_sum(1,3,5,7,9)
print(f)
print(f())
#在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
	
f=count()
print(f[0]())#返回值竟然是9
#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#返回函数不要引用任何循环变量，或者后续会发生变化的变量
		