import pygame
import os
import random
import time

class Mover():
	def __init__(self, x=None, y=None, direction=None, speed=None):
		self.x = x
		self.y = y
		self.w = 19
		self.h = 24
		self.hp = 2
		self.direction = 0
		self.speed = 0
		self.gold = 0
		self.jump = -1
		imageroot = "resources%splayer%s" % (os.sep,os.sep)
		self.media = {'idle':pygame.image.load(imageroot+"idle1.png"),
						'idle2':pygame.image.load(imageroot+"idle2.png"),
						'heart':pygame.image.load(imageroot+"heart.png"),
						'falling':pygame.image.load(imageroot+'falling.png')}
		self.image = self.media['idle']
		self.hand = None

	def loop(self, gameinfo=None, screen=None):
		self.gravity(gameinfo,3, 24)
		self.controls(pygame.key.get_pressed(), gameinfo, screen)

	def gravity(self, gameinfo=None, gravity=None, maxjump=None):	
		if self.jump > 0 and self.jump < maxjump:
			self.Move(gameinfo, 0, -gravity)
			if self.jump != -1:
				self.jump += 1
			if self.speed > 0: self.speed -= 0.1

		else:
			self.jump = -1
			self.Move(gameinfo, 0, gravity)
			if self.speed < 1:
				self.speed += 0.1


	def Move(self, gameinfo=None, x=None, y=None):
		if x>0:
			tempx = self.x + x 
			if gameinfo.gamemap.tile(round((tempx+(self.w-1))/32), round((self.y+1)/32)).soli == False and gameinfo.gamemap.tile(round((tempx+(self.w-1))/32), round((self.y+(self.h-1))/32)).soli == False:
				self.x = self.x + x
		
		if x<0:
			tempx = self.x + x 
			if gameinfo.gamemap.tile(round((tempx+1)/32), round((self.y+1)/32)).soli == False and gameinfo.gamemap.tile(round((tempx+1)/32), round((self.y+(self.h-1))/32)).soli == False:
				self.x = self.x + x
			
		if y>0:
			tempy = self.y + y 
			if gameinfo.gamemap.tile(round((self.x+1)/32), round((tempy+(self.h-1))/32)).soli == False and gameinfo.gamemap.tile(round((self.x+(self.w-1))/32), round((tempy+(self.h-1))/32)).soli == False:
				#Falling
				self.y = tempy
				self.speed += 0.1
				if self.speed > 2:
					self.image = self.media['falling']
			else:
				#Falling but stopped
				if self.speed >= 6:
					self.hp -= 1
					print "Ouch! HP currently at %s" % self.hp
					self.speed = 0
				self.speed = 0
				self.jump = 0
				self.image = self.media['idle']
			
		if y<0:
			#Jumping?
			tempy = self.y + y 
			if gameinfo.gamemap.tile(round((self.x+1)/32), round((tempy+1)/32)).soli == False and gameinfo.gamemap.tile(round((self.x+(self.w-1))/32), round((tempy+1)/32)).soli == False:
				self.y = tempy
			else:
				self.jump = -1

	def controls(self, key, gameinfo, screen):
		pygame.event.pump()
	
		move = 0

		if key[pygame.K_F12]:
			pygame.display.toggle_fullscreen()

		if key[pygame.K_TAB]:
			for ent in gameinfo.entlist.entlist:
				if ent.x == self.x/32 and ent.y == self.y/32:
					ent.use(gameinfo,self)

		if key[pygame.K_LSHIFT]:
			if self.hand != None:
				self.hand.use(gameinfo,self)

		if key[pygame.K_LEFT]: 
			self.Move(gameinfo, -1, 0)
			self.MOVE = 1

		elif key[pygame.K_RIGHT]: 
			self.Move(gameinfo, 1, 0)
			self.MOVE = 1		
	
		if key[pygame.K_SPACE]: 
			if self.jump == 0:
				self.jump = 1
		
		if key[pygame.K_z]:
			localtime = time.localtime()
			if os.path.isdir("screenshots") == False:
				os.makedirs("screenshots")
			pygame.image.save(screen, 'screenshots%sscr-%s-%s.%s.png' %(os.sep, localtime[3], localtime[4], localtime[5]))

		if key[pygame.K_ESCAPE]: 
			print "You had: %s that play\nGood job!" % self.gold
			exit()