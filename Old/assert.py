#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
a='0'
b=int(a)
logging.info('n=%d'%b)
print(10/b)


def foo(s):
	n=int(s)
	assert n!=0,'n is zero!'
	return 10/n
	
foo(0)