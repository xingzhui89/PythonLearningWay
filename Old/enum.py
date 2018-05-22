#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum,unique

@unique#装饰器保证没有重复值、
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6
	
for name,member in Weekday.__members__.items():
	print(name,'=>',member)