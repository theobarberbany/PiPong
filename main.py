from blessed import Terminal

t = Terminal()

def printBlockCenter():
	return(t.center(t.white_on_black(' ')).rstrip())

class screen(object):
	
	def __init__(self):
		pass	
	
	def drawNet(self):
		with t.fullscreen():
			for i in range(0, t.height,2):
				print(t.move_y(t.height - i) + printBlockCenter())
		t.inkey()

board = screen()
board.drawNet()
