import pygame
import os
import sys
import readmap
import time
import mover
import random
import math
import camera

pygame.init()
height = 320
width = 320
window = pygame.display.set_mode((height,width))
pygame.display.set_caption('PyLunky!')
screen = pygame.display.get_surface()
screen.convert_alpha()
clock = pygame.time.Clock()

def main():
	
	image = pygame.image.load('resources%sa.png' % os.sep)
	global gameinfo
	gameinfo = readmap.ReadMap('1.map')
	newmover = mover.Mover(x=gameinfo.gamemap.start[0]*32,y=gameinfo.gamemap.start[1]*32, direction=0, speed=0)

	cam = camera.cam(newmover.x, newmover.y, width, height, gameinfo.gamemap.width()*32, gameinfo.gamemap.height()*32)
	
	while True:
		pygame.event.pump()

		newmover.controls(pygame.key.get_pressed(), gameinfo, screen)
		newmover.gravity(gameinfo,4, 24)
		
		for k in gameinfo.gamemap.map():
			for i in k:						
				screen.blit(i.mat, (i.posx*32-cam.x,i.posy*32-cam.y))
		screen.blit(newmover.media['player'], (newmover.x-cam.x,newmover.y-cam.y))
		newmover.hpdisp(screen)

		cam.move(newmover.x, newmover.y)

		for ent in gameinfo.entlist.entlist:
			screen.blit(ent.mat, (ent.position()[0]-cam.x,ent.position()[1]-cam.y))
		pygame.display.flip()
		clock.tick(90)

main()
