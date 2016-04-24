from blessed import Terminal
import sys,os
import subprocess
t = Terminal()


print(t.height)
print(t.width)
print(t.white_on_black('Blue skies!'))
def printblock():
    return(t.center(t.white_on_black(' ')).rstrip())


with t.fullscreen():
    print(t.move_y(t.height - 2) + printblock()) 
    print(t.move_y(t.height - 4) + printblock())
    print(t.move_y(t.height - 6) + printblock())
    print(t.move_y(t.height - 8) + printblock())
    print(t.move_y(t.height - 10) + printblock())
    print(t.move_y(t.height - 12) + printblock())
    print(t.move_y(t.height - 14) + printblock())
    print(t.move_y(t.height - 16) + printblock())
    print(t.move_y(t.height - 18) + printblock())
    print(t.move_y(t.height - 20) + printblock())
    
    
    
    
    
    
    
    
    
    t.inkey()

