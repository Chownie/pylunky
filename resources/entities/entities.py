import random
import pygame
import os

class Entity():
	def __init__(self, x=None, y=None, hp=None, mat=None, name=None, text=None, width=None, height=None):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.hp = hp
		self.mat = mat
		self.name = name
		self.target = None
		self.text = text

	def move(self, x=None, y=None):
		self.x = x
		self.y = y

	def position(self):
		return (self.x*32,self.y*32)

	def debuginfo(self):
		print self.x
		print self.y
		print self.height
		print self.width
		print self.hp
		print self.mat
		print self.name
		print self.target
		print self.text

class Box(Entity):
	def use(self, gameinfo=None, player=None):
		namelist = ['gold','gem']
		name = random.choice(namelist)
		newent = entschema[random.choice(entschema.keys())]
		
		mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, newent['mat']))
		hp = newent['hp']

		x = self.x
		y = self.y

		height = newent['height']
		width = newent['width']
		text = ''

		print name
		entobj = newent['obj'](x,y,hp,mat,name,text,width,height)
		gameinfo.entlist.add(entobj)
		gameinfo.entlist.rem(self)

class Gold(Entity):
	def use(self, gameinfo=None, player=None):
		player.gold += random.randint(300,420)
		print player.gold
		gameinfo.entlist.rem(self)

class Gem(Entity):
	def use(self, gameinfo=None, player=None):
		player.gold += random.randint(150,250)
		print player.gold
		gameinfo.entlist.rem(self)

class Sign(Entity):
	def use(self,gameinfo=None, player=None):
		pass

entschema = {"box":{"hp":0,"mat":"box.png","width":12,"height":12,'obj':Box},
			"gold":{"hp":0,"mat":"gold.png","width":24,"height":8,'obj':Gold},
			"gem":{"hp":0,"mat":"gem.png","width":24,"height":8,'obj':Gem},
			"sign":{"hp":0,"mat":"sign.png","width":26,"height":26,'obj':Sign}}