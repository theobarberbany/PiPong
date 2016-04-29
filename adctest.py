import smbus
import time
I2CADDR = 0x21
bus = smbus.SMBus(1)
bus.write_byte( I2CADDR, 0x40 )
tmp = bus.read_word_data( I2CADDR, 0x00 ) 

tmp = tmp&61440
hi = tmp&255
lo = tmp&65280
r = 0

hi >> 8
lo << 8

r = hi | lo

print(r)
