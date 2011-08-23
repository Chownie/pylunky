import pygame

class Mover():
	def __init__(self, x, y, direction, speed, image):
		self.x = 0
		self.y = 0
		self.direction = 0
		self.speed = 0
		self.image = pygame.image.load('./resources/a.jpg')
