from blessed import Terminal
import random
import time
import logging

logging.basicConfig(filename = "game.log", level = logging.DEBUG, filemode = 'w')

t = Terminal()
print(t.fullscreen)
print(t.hidden_cursor)
print(t.clear)
def printbl(x, y):
	print(t.move_y(y) + t.move_x(x) + t.white_on_black(' '))

def printBlockCenter():
	return(t.center(t.white_on_black(' ')))
class Game(object):
	def __init__(self):
		self.ball = Ball()
		self.net = Net()
	def drawGame(self):
		self.ball.drawBall()
		self.net.drawNet()
	
	def updateGame(self):
		self.ball.updateBall()
	def resetGame(self):
		self.ball.resetBall()

	def startGame(self):
		self.resetGame()
		while True:
			self.drawGame()
			self.updateGame()
			time.sleep(1/30)
			print(t.clear)

class Net(object):
	
	def __init__(self):
		pass	
	
	def drawNet(self):
		for i in range(0, t.height,2):
			print(t.move_y(t.height - i) + printBlockCenter())
			
class Ball(object):
	def __init__(self):
		starting_velocities = [-1, 1]
		self.x_vel = random.choice(starting_velocities)
		self.y_vel = random.choice(starting_velocities)
	def drawBall(self):
		printbl(self.x_pos, self.y_pos)		
	def resetBall(self):
		self.y_pos = t.height // 2
		self.x_pos = t.width // 2
	def updateBall(self):
		logging.debug(" Y velocity: " + str(self.y_vel))
		logging.debug("X velocity: " + str(self.x_vel))
		self.y_pos += self.y_vel
		self.x_pos += self.x_vel
		logging.debug("self.y_pos"+ str(self.y_pos))
		logging.debug("self.x_pos" + str(self.x_pos))
game = Game()
game.startGame()