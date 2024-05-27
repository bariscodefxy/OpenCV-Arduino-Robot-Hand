from pyfirmata2 import SERVO, Arduino
import sys, platform

try:
	if platform.system() == "Linux":
		print("Detected Linux.")
		board = Arduino("/dev/ttyUSB0")
	elif platform.system() == "Windows":
		print("Detected Windows.")
		board = Arduino("COM3")
	else:
		print('This module doesn\'t support other OSes except Windows and Linux.')
		sys.exit()
except:
	print('Failed to connect Arduino')
	sys.exit()

servo_vertical_pin = 11
servo_horizontal_pin = 12

def rotate_servo(pin, angle):
    board.digital[pin].write(angle)

def rotate_horizontal(angle):
	rotate_servo(servo_horizontal_pin, angle)

def rotate_vertical(angle):
	rotate_servo(servo_vertical_pin, angle)

def init_pins():
	board.digital[servo_vertical_pin].mode = SERVO
	board.digital[servo_horizontal_pin].mode = SERVO

init_pins()