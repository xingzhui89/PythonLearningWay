#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	pass
	
class Mammal(Animal):
	pass
	
class Runnable(object):
	def run(self):
		print('Running...')
class Flyable(object):
	def fly(self):
		print('flying...')
		
		
class Bird(Animal):
	pass
	
class Dog(Mammal,Runnable):
	pass
	
class Bat(Mammal,Runnable):
	pass
	
class Parrot(Bird,Flyable):
	pass
	
class Ostrich(Bird,Flyable):
	pass
	
	
d=Dog()
d.run()
