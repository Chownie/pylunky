import pygame
#Standard lib
import os
import sys
import time
import random
import math
#Own Files
import readmap
import mover
import camera
import display

pygame.init()
height = 320
width = 320
window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
pygame.display.set_caption('PyLunky!')
screen = pygame.display.get_surface()
screen.convert_alpha()
clock = pygame.time.Clock()

def main():
	
	global gameinfo
	gameinfo = readmap.ReadMap('1.map')
	newmover = mover.Mover(x=gameinfo.gamemap.start[0]*32,y=gameinfo.gamemap.start[1]*32, direction=0, speed=0)

	cam = camera.cam(newmover.x, newmover.y, width, height, gameinfo.gamemap.width()*32, gameinfo.gamemap.height()*32)
	
	ui = display.display()

	while True:
		pygame.event.pump()

		newmover.loop(gameinfo, screen)

		#Gamemap display
		for k in gameinfo.gamemap.map():
			for i in k:						
				screen.blit(i.mat, (i.posx*32-cam.x,i.posy*32-cam.y))

		#Entity display
		for ent in gameinfo.entlist.entlist:
			offcount = (32-ent.height,32-ent.width)
			screen.blit(ent.mat, 
			(ent.position()[0]+offcount[0]/2-cam.x,
			ent.position()[1]+offcount[1]-cam.y))
		
		#Player display
		screen.blit(newmover.image, (newmover.x-cam.x,newmover.y-cam.y))

		#UI elements
		ui.ui(screen, cam, newmover, gameinfo)

		#Camera update
		cam.move(newmover.x, newmover.y)

		pygame.display.flip()
		clock.tick(90)

main()
