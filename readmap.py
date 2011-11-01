#!/usr/bin/env python
from resources.blocks.blocks import *
from resources.entities import *
import pygame
from pygame.locals import *
import os

class MapCell():
	def __init__(self, posx=None, posy=None, mat=None, trans=None, soli=None):
		self.mat = mat
		self.posx = posx
		self.posy = posy
		self.trans = trans
		self.soli = soli

class MapObj():
	def __init__(self, add):
		base = []
		splitmap = add.split('\n')
		for y in range(0,len(splitmap)):
			newbit = []
			for x in range(0,len(splitmap[y])):
				attri = blocks[splitmap[y][x]]
				mat = pygame.image.load('resources%sblocks%s%s'% (os.sep, os.sep, attri['mat']))
				soli = attri['soli']
				trans = attri['trans']
				newbit.append(MapCell(x,y,mat,trans,soli))
			base.append(newbit)
		self.mapinfo = base

	def tile(self, x, y):
		if x < 0 or x >= self.width() or y < 0 or y >= self.height():
			return MapCell(soli=True)
		else:
			return self.mapinfo[int(y)][int(x)]

	def map(self):
		return self.mapinfo

	def height(self):
		return len(self.mapinfo)

	def width(self):
		return len(self.mapinfo[0])

class EntMap():
	def __init__(self, text=None):
		rawentlist = text.split('\n')
		self.entlist = []

		del rawentlist[-1]

		for ent in rawentlist:
			print ent
			entinfo = ent.split(' ')
			entattri = entities.entschema[entinfo[0]]

			mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, entattri['mat']))
			hp = entattri['hp']
			x = int(entinfo[1])
			y = int(entinfo[2])
			self.entlist.append(entities.Entity(x,y,hp,mat))

	def count(self):
		return len(self.entlist)


class Entity():
	def __init__(self, x=None, y=None, hp=None, mat=None):
		self.x = x
		self.y = y
		self.hp = hp
		self.mat = mat

	def move(self, x=None, y=None):
		self.x = x
		self.y = y
	
class ReadMap():
	def __init__(self, file=None):
		f = open(file,'r')
		mapfile = f.read()
		f.close()
		
		self.gamemap = MapObj(mapfile.split('MAP\n')[1])
		self.entlist = EntMap(mapfile.split('ENT\n')[1].split('MAP\n')[0])
