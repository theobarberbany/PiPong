import sys
import time
import random

class screen (object):

    BASE_COLOUR = 40            #40=BLACK, base colour for backgroun
    
    def __init__ (self, width, height):
        self._width = width
        self._height= height

        self._rows = []

        for i in range(height):
            row = []
            for j in range(width):
                row.append(self.BASE_COLOUR)    #Create an array for every row, initialise to base colour value

            self._rows.append(row)

        self._print_screen()

    def draw_rectangle(self, x, y, w, h, colour):
        """
        Draw a w by h rectangle on the screen in the given colour at position (x,y)
        """

        for i in range(w):
            for j in range(h):
                self._update_pixel(x+i, y+j, colour)
        

    def _update_pixel(self, x, y, colour):

        sys.stdout.write(chr(27) + "[u")        #Load stored cursor position (Stored at initial print screen to avoid screen resizing issues
        sys.stdout.write(chr(27) + "[" + str(self._height + 1) + "A")   #Offset this position so that top-left is (0,0) (Move cursor up by height +1)

        sys.stdout.write(chr(27) + "[" + str(x) + "C")  #Move cursor forward by x
        sys.stdout.write(chr(27) + "[" + str(y) + "B")  #Move cursor down by y

        self.__print_block(colour)                      #print a single block in the current cursor position
        sys.stdout.write(chr(27) + "[u")                #Restore the original cursor position
        

    def _print_screen(self):     #DO NOT call this every frame; too slow. Called once in initilisation
        sys.stdout.write(chr(27) + "[2J")               #clear the screen
        sys.stdout.write(chr(27) + "[s")                #Save default cursor position
        for row in self._rows:
            self.__print_line(row)                      #print each line

    def __print_block(self, colour):
        sys.stdout.write("\x1b[" + str(colour) + "m \x1b[0m")       #print a single block of given colour
                                                                    #40=Black; 41=Red; 42=Green; 43=Yellow; 44=Blue; 45=Magenta; 46=Cyan; 47=White

    def __print_line(self, line_arr):                               #print a line of blocks given by an array of ints

        sys.stdout.write(chr(27) + "[" + str(1) + "C")              #Move the cursor one space forward (it starts in the "-1" slot for some reason)
        
        for i in range(0, len(line_arr)):                           
            self.__print_block(line_arr[i])

        sys.stdout.write('\n')                                      #New line
        

s = screen(80,10)
s.draw_rectangle(6, 3, 3, 5, 43)
s.draw_rectangle(5, 5, 1, 1, 45)

colours = [40,41,42,43,44,45,46,47]

while True:
    c = random.choice(colours)
    x = random.randrange(0, 81)
    y = random.randrange(0, 11)
    w = random.randrange(0, 81 - x + 1)
    h = random.randrange(0, 11 - y + 1)
    s.draw_rectangle(x, y, w, h, c)

print("")
