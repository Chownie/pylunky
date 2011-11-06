import pygame
import os
import random

pyload = pygame.image.load


bitlist = {"1":['1down.png','1up.png','1left.png','1right.png',
				'1upright.png','1upleft.png','1downright.png','1downleft.png'],
			"0":['0torch.png','0plant.png','blank.png','0hole.png']
			}

class Bitloader():
	"""Loading 'bits' (the extra polished parts) to map tiles"""
	def __init__(self):
		self.images = {}
		for tile in bitlist.keys():
			for img in bitlist[str(tile)]:
				if str(tile) in self.images.keys():
					self.images[str(tile)].append(pyload('resources%sblocks%sbits%s%s' % (os.sep,os.sep,os.sep,img)))
				else:
					self.images[str(tile)] = []
					self.images[str(tile)].append(pyload('resources%sblocks%sbits%s%s' % (os.sep,os.sep,os.sep,img)))

	def setoverlay(self, tile=None, mapinfo=None, bitdict=None, bittype=None):
		types = bittype.split(':')
		for section in types:
			if bittype == None:
				tile.mat = tile.mat
			elif bittype == "random":
				tile.mat.blit(random.choice(bitdict[str(tile.name)]),(0,0))
			elif bittype == "floor":
				if mapinfo.tile(tile.posx,tile.posy+1).soli == True:
					tile.mat.blit(random.choice(bitdict[str(tile.name)]),(0,0))
			elif bittype == "border":
				if mapinfo.tile(tile.posx-1,tile.posy).name != tile.name:
					tile.mat.blit(bitdict[str(tile.name)][2],(0,0))
				if mapinfo.tile(tile.posx+1,tile.posy).name != tile.name:
					tile.mat.blit(bitdict[str(tile.name)][3],(0,0))
				if mapinfo.tile(tile.posx,tile.posy-1).name != tile.name:
					tile.mat.blit(bitdict[str(tile.name)][1],(0,0))
				if mapinfo.tile(tile.posx,tile.posy+1).name != tile.name:
					tile.mat.blit(bitdict[str(tile.name)][0],(0,0))

				#Diagonals

				if mapinfo.tile(tile.posx+1,tile.posy-1).name != tile.name: # Up-right
					tile.mat.blit(bitdict[str(tile.name)][4],(0,0))

				if mapinfo.tile(tile.posx-1,tile.posy+1).name != tile.name: # Down-left
					tile.mat.blit(bitdict[str(tile.name)][7],(0,0))
				
				if mapinfo.tile(tile.posx-1,tile.posy-1).name != tile.name: # Up-Left
					tile.mat.blit(bitdict[str(tile.name)][5],(0,0))
				
				if mapinfo.tile(tile.posx+1,tile.posy+1).name != tile.name: # Down-Right
					tile.mat.blit(bitdict[str(tile.name)][6],(0,0))