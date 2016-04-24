from blessed import Terminal
import sys,os
import subprocess
subprocess.Popen("\e[40m")
t = Terminal()

print(t.height)
print(t.width)
print(t.white_on_black('Blue skies!'))

term = Terminal()
with term.fullscreen():
    blue()
    print(term.move_y(term.height // 2) +
          term.center(term.white_on_black('press any key')).rstrip())
    term.inkey()

