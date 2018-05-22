#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper


@log
def now():
	print('2017-11-02')
now()
print(now.__name__)
#print(dir(now))

