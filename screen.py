import sys
import time
import random

COLOUR_BLACK = 40
COLOUR_RED = 41
COLOUR_GREEN = 42
COLOUR_YELLOW = 43
COLOUR_BLUE = 44
COLOUR_MAGENTA = 45
COLOUR_CYAN = 46
COLOUR_WHITE = 47

class screen (object):

    BASE_COLOUR = COLOUR_WHITE                   #40=BLACK, base colour for background
    NET_COLOUR = COLOUR_BLACK
    
    def __init__ (self, width, height):
        self._width = width
        self._height= height

        self._rows = []

        for i in range(height):
            row = []
            for j in range(width):
                if(j == width / 2 and not i % 3 == 0):
                    row.append(self.NET_COLOUR)
                else:
                    row.append(self.BASE_COLOUR)    #Create an array for every row, initialise to base colour value

            self._rows.append(row)

        self._print_screen()

    def _on_screen(self, x, y):
        """
        Returns True is the given point is within the bounds of the screen
        """
        if( x >= 0 and x <= self._width and y >= 0 and y <= self._height):
            return True

        return False

    def draw_rectangle(self, x, y, w, h, colour):
        """
        Draw a w by h rectangle on the screen in the given colour at position (x,y)
        """
        
        
        for i in range(w+1):
            for j in range(h+1):
                self._update_pixel(x+i, y+j, colour)

    def get_default_pixel_value(self, x,y):
        """
        Returns the default value of he pixel at (x,y)
        """
        return self._rows[y][x-1]

    def draw_number(self, x, y, number, colour = COLOUR_WHITE, trim_colour = COLOUR_BLACK):
        """
        Draws a number contained within a 3x5 rectangle, anchored top left at position (x,y)
        number: int
        """

        if(number == 0):
            self._draw_0(x,y,colour,trim_colour)
        if(number == 1):
            self._draw_1(x,y,colour,trim_colour)
        if(number == 2):
            self._draw_2(x,y,colour,trim_colour)
        if(number == 3):
            self._draw_3(x,y,colour,trim_colour)
        if(number == 4):
            self._draw_4(x,y,colour,trim_colour)
        if(number == 5):
            self._draw_5(x,y,colour,trim_colour)
        if(number == 6):
            self._draw_6(x,y,colour,trim_colour)
        if(number == 7):
            self._draw_7(x,y,colour,trim_colour)
        if(number == 8):
            self._draw_8(x,y,colour,trim_colour)
        if(number == 9):
            self._draw_9(x,y,colour,trim_colour)

    def _draw_0(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x+1, y+1, 1,2, tcol)

    def _draw_1(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, tcol)
        self.draw_rectangle( x+1, y, 1, 4, col)

    def _draw_2(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x, y+1, 2, 0, tcol)
        self.draw_rectangle( x+2, y+3, 2, 0, tcol)

    def _draw_3(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x, y+1, 2, 0, tcol)
        self.draw_rectangle( x, y+3, 2, 0, tcol)

    def _draw_4(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x+1, y, 1, 1, tcol)
        self.draw_rectangle( x, y+3, 2, 2, tcol)

    def _draw_5(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x+1, y+1, 2, 0, tcol)
        self.draw_rectangle( x, y+3, 2, 0, tcol)

    def _draw_6(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x+1, y+1, 2, 0, tcol)
        self.draw_rectangle( x+1, y+3, 1, 0, tcol)

    def _draw_7(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x, y+1, 2, 3, tcol)

    def _draw_8(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x+1, y+1, 1, 0, tcol)
        self.draw_rectangle( x+1, y+3, 1, 0, tcol)

    def _draw_9(self, x, y, col, tcol):
        self.draw_rectangle( x, y, 3, 4, col)
        self.draw_rectangle( x+1, y+1, 1, 0, tcol)
        self.draw_rectangle( x, y+3, 2, 1, tcol)

    def _update_pixel(self, x, y, colour):

        self.output(chr(27) + "[u")                #Load stored cursor position (Stored at initial print screen to avoid screen resizing issues
        self.output(chr(27) + "[" + str(1) + "A")
        
        self.output(chr(27) + "[" + str(x) + "C")  #Move cursor forward by x
        self.output(chr(27) + "[" + str(y) + "B")  #Move cursor down by y

        self.__print_block(colour)                      #print a single block in the current cursor position
        self.output(chr(27) + "[u")                #Restore the original cursor position

    def _move_pixel(self, x_new, y_new, colour, x_prev, y_prev):
    	self._update_pixel(x_new, y_new, colour)
        if(self._on_screen(x_prev, y_prev)):
		print("On Screen trued: " + str(x_prev) + "   ,     " + str(y_prev))
		self._reset_pixel(x_prev, y_prev)


    def _move_rectangle(self, x_new, y_new, w_new, h_new, colour,x_prev, y_prev, w_prev, h_prev):
        """
        Delete the rectangle described by prev and draw the rectangle described by new
        """
        self._reset_rectangle(x_prev, y_prev, w_prev, h_prev)
        self.draw_rectangle(x_new, y_new, w_new, h_new, colour)        

    def _reset_rectangle(self, x,y,w,h):
        for i in range(w+1):
            for j in range(h):
                self._reset_pixel(i+x, j+y)

    def _reset_pixel(self, x, y):
        """
        Resets a single pixel to its default value as stored in the screen rows array
        """
	try:
        	self._update_pixel(x,y,self.get_default_pixel_value(x,y-1))
	except IndexError:
		print("Pixel: " + str(x) + "    ,     " + str(y) + "\n\n\n\n\n\n\n\n\n\n")
		raise IndexError


    def _print_screen(self):                            #DO NOT call this every frame; too slow. Called once in initilisation
        sys.stdout.write(chr(27) + "[?25l")
        sys.stdout.write(chr(27) + "[2J")               #clear the screen
        sys.stdout.write(chr(27) + "[s")                #Save default cursor position
        for row in self._rows:
            self.__print_line(row)                      #print each line

    def __print_block(self, colour):
        self.output("\x1b[" + str(colour) + "m \x1b[0m")       #print a single block of given colour
                                                                    #40=Black; 41=Red; 42=Green; 43=Yellow; 44=Blue; 45=Magenta; 46=Cyan; 47=White

    def __print_line(self, line_arr):                               #print a line of blocks given by an array of ints

        self.output(chr(27) + "[" + str(1) + "C")              #Move the cursor one space forward (it starts in the "-1" slot for some reason)
        
        for i in range(0, len(line_arr)):                           
            self.__print_block(line_arr[i])

        sys.stdout.write('\n')                                      #New line

    def _gui_delay(self, t):
        """
        Delay for t seconds, GUI safe
        """
        s = time.time()

        while (time.time() - s) < t:
            self.output(chr(27) + "[" + str(0) + "C")              #NOP

    def output(self, msg):
        """
        OUTPUT message to terminal
        """
        #TODO-serial integration




        #For testing:
        sys.stdout.write(msg)
        
    

s = screen(80,40)

######TEST - Moving rectangles
##x = 3
##y = 0
##w = 0
##h = 4
##while True:
##    s._move_rectangle(x, y, w, h, COLOUR_YELLOW ,x, y - 1, w, h)
##    s._move_rectangle(80-x, y, w, h, COLOUR_YELLOW ,80-x, y - 1, w, h)
##
##    y += 1
##    
##    s._gui_delay(0.05)

####TEST - Moving pixels
##x = 0
##y = 0
##while True:
##    s._move_pixel(x, y, COLOUR_YELLOW ,x-2, y - 1)
##
##    x += 2
##    y += 1
##    
##    s._gui_delay(0.1)

##TEST - Print Numbers
#for i in range(10):
#    
#    s.draw_number(29, 2, i, COLOUR_CYAN)
#    s.draw_number(51, 2, i, COLOUR_YELLOW)

#    s._gui_delay(1)


s.draw_rectangle(0,40,1,0,43)
#s.draw_rectangle(3,3,3,5,46)
#s.draw_rectangle(0,0,1,1,45)

##s.draw_rectangle(5, 5, 5, 5, 45)
##s._reset_rectangle(5,5,2,2)

####TEST - Generate random rectangles
##while True:
##    c = random.choice(colours)
##    x = random.randrange(0, 81)
##    y = random.randrange(0, 11)
##    w = random.randrange(0, 81 - x)
##    h = random.randrange(0, 11 - y)
##    s.draw_rectangle(x, y, w, h, c)





#while True:
#    sys.stdout.write(chr(27) + "[" + str(0) + "C")                  #NOP to keep screen updated

