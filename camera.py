class cam():
	def __init__(self, x=0, y=0, height=0, width=0):
		self.x = 0
		self.y = 0
		self.width = width
		self.height = height
		print "H: %s | W: %s" %  (self.height, self.width)
	def move(self, x, y):
		tempx = x-self.width/2
		tempy = y-self.height/2

		#WHY DOES THIS WORK? I DON'T UNDERSTAND
		#MAGIC?
		if tempx > 0 and tempx+self.width/2 < self.width:
			self.x = tempx

		#this doesn't work
		#uses exactly the same condition as above with the same set of variables
		#it is a mystery
		if tempy > 0 and tempy+self.height/2 < self.height:
			self.y = tempy
