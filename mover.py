import pygame
import os

class Mover():
	def __init__(self, x, y, direction, speed, image):
		self.x = 0
		self.y = 0
		self.w = 32
		self.h = 32
		self.direction = 0
		self.speed = 0
		self.jump = -1
		self.image = pygame.image.load('./resources/a.png')