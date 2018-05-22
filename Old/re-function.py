#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
		
print(fact(10))
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):

    if n == 1:

        print('move', a, '-->', c)

    else:

        move(n-1, a, c, b)

        move(1, a, b, c)

        move(n-1, b, a, c)



move(4, 'A', 'B', 'C')