#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python内置的sorted()函数就可以对list进行排序
print(sorted([36,5,-9,29]))
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([36,5,-9,29],key=abs,reverse=True))#如果设定reverse，那么就是从大到小排列了
print(sorted(['Boc','about','lisa'],key=str.lower))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
L2 = sorted(L, key=by_name)
print(L2)