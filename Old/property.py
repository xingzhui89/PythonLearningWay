#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	@property#将方法变成属性
	def age(self):
		return self.__age
	
	@property
	def score(self):
		return self.__score
	
	@score.setter
	def score(self,score):
		if not isinstance(score,int):
			raise ValueError('score must be an integer!')
		if score<0 or score>100:
			raise ValueError('score must between 0~100!')
		self.__score=score

		
s=Student()
s.score=60
print(s.score)
print(dir(Student))

