class cam():
	def __init__(self, x=0, y=0, width=0, height=0, mapw = 0, maph = 0):
		self.x = 0
		self.y = 0
		self.width = width
		self.height = height
		self.mapw = mapw
		self.maph = maph
		print "H: %s | W: %s" %  (self.height, self.width)

	def move(self, x, y):
		"""Move the camera to where the player is, lock to the corners of the map"""
		if x-self.width/2 > 0 and x+self.width/2 < self.mapw:
				self.x = x-self.width/2
		if y-self.height/2 > 0 and y+self.height/2 < self.maph:
				self.y = y-self.height/2
