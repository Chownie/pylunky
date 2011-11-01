entschema = {"box":{"hp":0,"mat":"box.png"}}

class Entity():
	def __init__(self, x=None, y=None, hp=None, mat=None):
		self.x = x
		self.y = y
		self.hp = hp
		self.mat = mat
		self.loose = True

	def move(self, x=None, y=None):
		self.x = x
		self.y = y

	def attach(self, target=None):
		if target != None:
			print "Attatched!"
			self.target = target
			self.loose = False

	def position(self):
		if self.loose == False:
			self.x = self.target.x
			self.y = self.target.y
			return (self.x,self.y)
		else:
			return (self.x*32,self.y*32)