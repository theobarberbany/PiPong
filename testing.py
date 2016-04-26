from blessed import Terminal
import sys,os
import subprocess
t = Terminal()



def printtest(x,y):
	print(t.move(x,y) + t.white_on_black('.'))

def printblock():
	return(t.center(t.white_on_black(' ')).rstrip())

def printbl(x, y):
	print(t.move_y(y) + t.move_x(x) + t.white_on_black(' ').rstrip())
with t.fullscreen():
#	for i in range(0,t.height,2):
#		print(t.move_y(t.height- i) + printblock())
##
	printtest(15,12)
	

