import screen
#import interface
import time
import random

#TEMP - for keyboard testing controls
#import kbtest
cur_pos0 = 0
cur_pos1 = 0

class game(object):

    def __init__(self,game_board_w, game_board_h):
        self._width = game_board_w
        self._height = game_board_h
        self._score0 = 0
        self._score1 = 0

    def start(self):
        self._s = screen.screen(self._width, self._height)                #Create a new screen with the supplied width and height

        #self._player0_bat = bat(self._s, 0)
        #self._player1_bat = bat(self._s, 1, screen.COLOUR_CYAN)

        self._ball = ball(self._s, self, screen.COLOUR_YELLOW)
        self._ball.set_velocity(1, 1)
        
        while True:
            self._s.output(chr(27) + "[" + str(0) + "C")                  #NOP to keep screen updated

##            self._player0_bat.set_bat_position(self.get_input(0))                           #Retrieve player input and set the bat positions
##            self._player1_bat.set_bat_position(self.get_input(1))

            self._ball.add_velocity()
            self._ball.draw()
            
##            #TEMP - Quit Button t
##            if(kbtest.getch() == 't'):          
##                break

            self._s._gui_delay(0.06)


    def update_score(self, player, new_score):
        n=1
        if(player == 0):
            n=-1
        
        self._s.draw_number((self._width / 2) + n*8, 2, new_score)          #Draws the new_score as a 3x5 number in the specified position (8 away from the net)

    def get_input(self, player):
        """
        Get input from the player. Players e {0,1}
        """
        #TODO - Interface with hardware



        #TEMP - KEYBOARD CONTROLS

        global cur_pos0
        global cur_pos1
        
        if(player == 0):
            
            if(kbtest.player0_up() and cur_pos0 < self._height - 1):
                cur_pos0 += 1
            if(kbtest.player0_down() and cur_pos0 > 3):
                cur_pos0 -= 1
            
            return cur_pos0

        if(kbtest.player1_up() and cur_pos1 < self._height - 1):
            cur_pos1 += 1
        if(kbtest.player1_down() and cur_pos1 > 3):
            cur_pos1 -= 1

        return cur_pos1
        
            
        

class bat(object):
    
    def __init__(self, screen, player, colour = screen.COLOUR_YELLOW):
        self._player = player
        self._screen = screen
        self._colour = colour
        self._position = 0
        self._prev_position = -1                                    #Used to ensure redrawing only occurs when the bat moves

        self.draw_bat()

    def draw_bat(self):
        if(self._prev_position == self._position):                  #Don't redraw the bat if it has not moved
            return
        
        x = 3
        if(self._player == 1):
            x = self._screen._width - 3                             #Generate the x value of the bat based on which player the bat belongs to

        self._screen._move_rectangle(x, self._position, 0, 3, self._colour, x, self._prev_position, 0, 3) #Move the bat (removes old bat and redraws in the new position)
        self._prev_position = self._position

    def set_bat_position(self, position):
        self._position = position
        self.draw_bat()

class ball(object):

    def __init__(self, screen, game, colour):
        self._screen = screen
        self._x_vel = 0
        self._y_vel = 0
        self._x_pos = 4
        self._y_pos = 2
        self._x_pow = 1
        self._y_pow = 1
        self._colour = colour

    def set_velocity(self, x, y):
        """
        Set the x and y velocties of the ball
        """
        self._x_vel = x
        self._y_vel = y

    def add_velocity(self):
        """
        Add the stored x and y velocities to the ball's position
        """
        #Collision Detection
        w = self._screen._width
        h = self._screen._height
        x = self._x_pos
        y = self._y_pos
        nx = self._x_pos + self._x_vel
        ny = self._y_pos + self._y_vel      #new x and y values
        
        if(ny <= 0 or ny > h):
            if(random.randrange(0, 3) == 1 ):       #1 in 3 chance to double speed 
                self._y_pow = 2
            else:
                self._y_pow = 1                
                
            self.set_velocity( self._x_vel, -self._y_vel )

        if(nx < 3 or nx > w - 3):
                                            #Check if a bat is occupying the new position, if it is, rebound, else player on opposite side gains a point
            

            
            
            if(random.randrange(0, 3) == 1 ):
                self._x_pow = 2
            else:
                self._x_pow = 1 
                
            self.set_velocity( -self._x_vel, self._y_vel )


        #Velocity Change
        self._x_prev = self._x_pos
        self._y_prev = self._y_pos
        
        self._x_pos += self._x_vel * self._x_pow
        self._y_pos += self._y_vel * self._y_pow

    def draw(self):
        """
        Draw the ball.
        """
        self._screen._move_pixel(int(self._x_pos), int(self._y_pos), self._colour, int(self._x_prev), int(self._y_prev))
        

    

g = game(80, 40)
g.start()


