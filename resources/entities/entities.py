entschema = {"box":{"hp":0,"mat":"box.png"}}

class Entity():
	def __init__(self, x=None, y=None, hp=None, mat=None, name=None):
		self.x = x
		self.y = y
		self.hp = hp
		self.mat = mat
		self.name = name
		self.target = None

	def move(self, x=None, y=None):
		self.x = x
		self.y = y

	def held(self, target=None):
		print self.target
		if target != None:
			self.target = target

	def position(self):
		if self.target != None:
			print self.target
			self.x = self.target.x
			self.y = self.target.y
			return (self.x,self.y)
		else:
			return (self.x*32,self.y*32)