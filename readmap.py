#!/usr/bin/env python
from resources.blocks import *
import pygame
from pygame.locals import *
import os

class mapCell(pygame.sprite.Sprite):
	def __init__(self, posx=None, posy=None, mat=None, trans=None, soli=None):
		self.mat = mat
		self.posx = posx
		self.posy = posy
		self.trans = trans
		self.soli = soli

class mapObj():
	def __init__(self, add):
		base = [[],[],[],[],[],[],[],[],[],[]]
		mapvar = add
		splitmap = mapvar.split('\n')
		for y in range(0,mapvar.count('\n')):
			for x in range(0,len(splitmap[y])):
				attri = blocks[splitmap[y][x]]
				mat = pygame.image.load('resources%s%s'% (os.sep, attri['mat']))
				soli = attri['soli']
				trans = attri['trans']
				base[x].append(mapCell(x,y,mat,trans,soli))
		self.mapinfo = base

	def tile(self, x, y):
		return self.mapinfo[y][x]

	def map(self):
		return self.mapinfo

	def height(self):
		return len(self.mapinfo)

	def width(self):
		return len(self.mapinfo[0][0])
