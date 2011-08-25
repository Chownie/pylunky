import pygame
import os
import sys
from readmap import *
import time
import mover
import random
import math

pygame.init()
window = pygame.display.set_mode((320,320))
pygame.display.set_caption('PyLunky!')
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

global collisions

def controls(key, puppet, mapinfo):
	pygame.event.pump()
	
	if key[pygame.K_LEFT]: 
		tempx = puppet.x-1
		tile = mapinfo[int(round(puppet.y+16/32))/32][int(round(tempx+16/32))/32]
		puppet.x-=collide(tile)

	elif key[pygame.K_RIGHT]: 
		tempx = puppet.x+32
		tile = mapinfo[int(round(puppet.y+16/32))/32][int(round(tempx+16/32))/32]
		puppet.x+=collide(tile)

	if key[pygame.K_UP]:
		tempy = puppet.y-1
		tile = mapinfo[int(round(tempy+16/32))/32][int(round(puppet.x+16/32))/32]
		puppet.y-=collide(tile)

	elif key[pygame.K_DOWN]: 
		tempy = puppet.y+32
		tile = mapinfo[int(round(tempy+16/32))/32][int(round(puppet.x+16/32))/32]
		puppet.y+=collide(tile)
		
	if key[pygame.K_ESCAPE]: exit()

def collide(tile):
	if tile.soli == False:
		print "FREE: "+str((tile.posx, tile.posy))
		return 1
	else:
		print "COLLIDE: "+str((tile.posx, tile.posy))
		return 0

def main():
	newmover = mover.Mover(x=12,y=12, direction=0, speed=0, image=pygame.image.load('resources%sa.jpg' % os.sep))
	mapfile = open('1.map','r').read()
	mapinfo = rMap(mapfile)

	while True:
		pygame.event.pump()
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]: pygame.image.save(screen, 'screenshot.png')
		controls(key, newmover, mapinfo)

		for k in mapinfo:
			for i in k:						
				screen.blit(i.mat, (i.posx*32,i.posy*32))
		screen.blit(newmover.image, (newmover.x,newmover.y))
		pygame.display.flip()
		clock.tick(60)

main()
