import pygame
import os
import random
import time
import font

class display():
	def __init__(self):
		self.textfont = pygame.image.load('resources%s%s' % (os.sep, 'font-12x16.png'))

	def ui(self, screen=None, camera=None, player=None, gameinfo=None):
		self.sign(screen,camera,gameinfo,player)
		self.showent(screen,camera,gameinfo)
		self.hpdisp(screen,player)
		self.gameover(screen,player)
		screen.blit(self.textfont,(0,0))

	def showent(self, screen=None,cam=None,gameinfo=None):
		for ent in gameinfo.entlist.entlist:
			print ent.name
			fontsize = font.size(ent.name)
			offcount = (32-ent.width,32-ent.height-8)

			position = (ent.position()[0]-fontsize[0]/2+fontsize[0]-cam.x,
			ent.position()[1]+fontsize[1]/2-fontsize[1]-cam.y)

			result = pygame.Surface((fontsize[0]+4, fontsize[1]+4), pygame.SRCALPHA)
			result.fill((90,90,90,40))
			result.blit(font.render(self.textfont,ent.name),(2,2))
			screen.blit(result,position)

	def sign(self,screen=None,cam=None,gameinfo=None,player=None):
		for ent in gameinfo.entlist.entlist:
			if ent.x == player.x/32 and ent.y == player.y/32 and ent.text != '':
				fontsize = font.size(ent.text)
				offcount = (32-ent.width,32-ent.height-8)

				result = pygame.Surface((fontsize[0]+4, fontsize[1]+4), pygame.SRCALPHA)
				result.fill((90,90,90,255))
				result.blit(font.render(self.textfont,ent.name),(2,2))
				screen.blit(result,(150,250))

	def hpdisp(self, screen=None, player=None):
		count = 0
		jiggle = 12
		for i in range(0,player.hp):
			if player.hp < 6: jiggle = random.randint(12,13)
			screen.blit(player.media['heart'],(count+14,jiggle))
			count += 12

#	def golddisp(self, screen=None, player=None):

	def gameover(self,screen=None,player=None):
		if player.hp == 0:
			screen.fill((0,0,0))
			text = "You have died"
			x=260-font.size(text)[0]
			screen.blit(font.render(text, False, (255,255,255)),(x,300))
			del player
		