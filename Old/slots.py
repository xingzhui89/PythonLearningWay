#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	pass
	
s=Student()
s.name='Michael'
print(s.name)


def set_age(self,age):
	self.age=age

def set_score(self,score):
	self.score=score

from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

Student.set_score=set_score

s.set_score(100)

print(dir(s))
print(dir(Student))
