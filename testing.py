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
mylist = [(1,3),(22,8),(44,20)]
for args in mylist:
	printtest(*args)

