import pygame
import os
import sys
import readmap
import time
import mover
import random
import math

pygame.init()
height, width = (320,320)
window = pygame.display.set_mode((height,width))
pygame.display.set_caption('PyLunky!')
screen = pygame.display.get_surface()
screen.convert_alpha()
clock = pygame.time.Clock()

global collisions

def gTile(x, y):
	return mapinfo.tile(x,y)

def oMove(o, x, y):	
	
	if x>0:
		tempx = o.x + x 
		if gTile(round((tempx+o.w)/32), round((o.y+o.h)/32)).soli == False and gTile(round((tempx+o.w)/32), round((o.y+o.h)/32)).soli == False:
			o.x = o.x + x
		
	if x<0:
		tempx = o.x + x 
		if gTile(round((tempx+1)/32), round((o.y+o.h)/32)).soli == False and gTile(round((tempx+1)/32), round((o.y+o.h)/32)).soli == False:
			o.x = o.x + x
			
	if y>0:
		tempy = o.y + y 
		if gTile(round((o.x+o.w)/32), round((tempy+o.h)/32)).soli == False and gTile(round((o.x+o.w)/32), round((tempy+o.h)/32)).soli == False:
			o.y = tempy
		else:
			o.jump = 0
			
	if y<0:
		tempy = o.y + y 
		if gTile(round((o.x+o.w)/32), round((tempy+1)/32)).soli == False and gTile(round((o.x+o.w)/32), round((tempy+1)/32)).soli == False:
			o.y = tempy
		else:
			o.jump = -1		

				
def gravity(o, gravity, maxjump):	
	if o.jump > 0 and o.jump < maxjump:
		oMove(o, 0, -gravity)
		if o.jump != -1:
			o.jump += 1
		if o.speed > 0: o.speed -= 0.1

	else:
		o.jump = -1
		oMove(o, 0, gravity)
		if o.speed < 1: o.speed += 0.1


def controls(key, o):
	pygame.event.pump()
	
	move = 0
	
	if key[pygame.K_LEFT]: 
		oMove(o, -1, 0)
		move = 1

	elif key[pygame.K_RIGHT]: 
		oMove(o, 1, 0)
		move = 1
		
	if key[pygame.K_UP]:
		oMove(o, 0, -1)
		move = 1

	elif key[pygame.K_DOWN]: 
		oMove(o, 0, 1)
		move = 1
	
	if key[pygame.K_SPACE]: 
		if o.jump == 0:
			o.jump = 1
		
	if key[pygame.K_s]:
		pygame.image.save(screen, 'screenshot.png')

	if key[pygame.K_ESCAPE]: exit()
	
			
def main():
	global mapinfo
	
	image = pygame.image.load('resources%sa.png' % os.sep)
	newmover = mover.Mover(x=12,y=12, direction=0, speed=0, image=image.convert_alpha())
	mapinfo = readmap.MapObj('1.map')

	while True:
		pygame.event.pump()
		key = pygame.key.get_pressed()
		#if key[pygame.K_SPACE]: pygame.image.save(screen, 'screenshot.png')
		controls(key, newmover)
		gravity(newmover, 4, 32)

		
		for k in mapinfo.map():
			for i in k:						
				screen.blit(i.mat, (i.posx*32,i.posy*32))
		screen.blit(newmover.image, (newmover.x,newmover.y))
		
		pygame.display.flip()
		clock.tick(90)

main()
