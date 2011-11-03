import pygame
import os

class Mover():
	def __init__(self, x=None, y=None, direction=None, speed=None):
		self.x = x
		self.y = y
		self.w = 19
		self.h = 24
		self.hp = 10
		self.direction = 0
		self.speed = 0
		self.jump = -1
		imageroot = "resources%splayer%s" % (os.sep,os.sep)
		self.media = {'player':pygame.image.load(imageroot+"player.png"),
						'heart':pygame.image.load(imageroot+"heart.png")}
		self.hand = None

	def hpdisp(self, screen=None):
		count = 0
		for i in range(0,self.hp):
			screen.blit(self.media['heart'],(count+14,12))
			count += 12
			

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
				self.y = tempy
				self.speed += 0.1
			else:
				if self.speed >= 6:
					self.hp -= 1
					print "Ouch! HP currently at %s" % self.hp
					self.speed = 0
				self.speed = 0
				self.jump = 0
			
		if y<0:
			tempy = self.y + y 
			if gameinfo.gamemap.tile(round((self.x+1)/32), round((tempy+1)/32)).soli == False and gameinfo.gamemap.tile(round((self.x+(self.w-1))/32), round((tempy+1)/32)).soli == False:
				self.y = tempy
			else:
				self.jump = -1

	def controls(self, key, gameinfo, screen):
		pygame.event.pump()
	
		move = 0
	
		if key[pygame.K_TAB]:
			if self.hand == None:
				for ent in gameinfo.entlist.entlist:
					if ent.x == self.x/32 and ent.y == self.y/32:
						print ent.x
						print ent.y

		if key[pygame.K_LALT]:
			print "x: %s" % self.x
			print "y: %s" % self.y
			print "direction: %s " % self.direction
			print "hp: %s" % self.hp

		if key[pygame.K_LSHIFT] and key[pygame.K_TAB]:
			print "Dropping item!"
			gameinfo.entlist.add(self.hand)
			self.hand = None

		if key[pygame.K_LEFT]: 
			self.Move(gameinfo, -1, 0)
			self.MOVE = 1

		elif key[pygame.K_RIGHT]: 
			self.Move(gameinfo, 1, 0)
			self.MOVE = 1		

		if key[pygame.K_DOWN]: 
			self.Move(gameinfo, 0, 1)
			self.MOVE = 1
	
		if key[pygame.K_SPACE]: 
			if self.jump == 0:
				self.jump = 1
		
		if key[pygame.K_z]:
			pygame.image.save(screen, 'screenshot.png')

		if key[pygame.K_ESCAPE]: exit()