#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
r=move(100,100,60,math.pi/6)
print(r)
#返回多值的时候，其实是返回了一个tuple

print(max(1,2,3,4,19,8))

def nop():
	pass

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-9))

def power(x,n=2):#默认参数必须指向不变对象
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

def calc(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

print(calc(1,2,3))
nums=[1,2,3]
print(calc(*nums))

def person(name,age,**kw)#关键字参数,其实就是一个dict
	print('name:',name,'age:',age,'other:',kw)
