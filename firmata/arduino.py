from pyfirmata import Arduino, SERVO
import sys

try:
	board = Arduino("/dev/ttyUSB0")
except:
	print('Failed to connect Arduino')
	sys.exit()

servo_floor_pin = 13
servo_horizontal_pin = 12

def rotate_servo(pin, angle):
    board.digital[pin].write(angle)

def rotate_horizontal(angle):
	rotate_servo(servo_horizontal_pin, angle)

def rotate_vertical(angle):
	rotate_servo(servo_floor_pin, angle)

def init_pins():
	board.digital[servo_floor_pin].mode = SERVO
	board.digital[servo_horizontal_pin].mode = SERVO