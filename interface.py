import smbus
import time
I2CADDR = 0x21
bus = smbus.SMBus(1)

def get_paddle_position(paddle):
	raw_value = get_pot_value(paddle)
	
	return raw_value / 15


def get_pot_value(paddle):

	bus.write_byte( I2CADDR, 0x40 )
	tmp = bus.read_word_data( I2CADDR, 0x00 ) 

	#tmp = tmp&61440
	lo = tmp&255
	hi = tmp&65280
	r = 0

	hi >> 8
	lo << 8

	r = hi | lo

	r = r&15

	return r


while True:
	print(get_paddle_position(0))
