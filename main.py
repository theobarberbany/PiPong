from blessed import Terminal

t = Terminal()

class Screen(object, fps):
	
	def __init__(self, fps):
		self.framerate = fps
	#Mutators
	
	def setFrameRate(self, fps):
		self.framerate = fps
	#Accessors

	def getFrameRate(self):
		return(self.framerate)
	def getHeight(self):
		return(t.height)
	def getWidth(self):
		return(t.width)	
		
