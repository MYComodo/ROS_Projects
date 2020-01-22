#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pin_i1 = 23
pin_i2 = 24
pin_i3 = 27
pin_i4 = 17

# Set the GPIO Pin mode to be Output
GPIO.setup(pin_i1, GPIO.OUT)
GPIO.setup(pin_i2, GPIO.OUT)
GPIO.setup(pin_i3, GPIO.OUT)
GPIO.setup(pin_i4, GPIO.OUT)

# Turn all motors off
def StopMotors():
    GPIO.output(pin_i1, GPIO.LOW)
    GPIO.output(pin_i2, GPIO.LOW)
    GPIO.output(pin_i3, GPIO.LOW)
    GPIO.output(pin_i4, GPIO.LOW)

# Turn both motors forwards
def Forwards():
    GPIO.output(pin_i1, GPIO.HIGH)
    GPIO.output(pin_i2, GPIO.LOW)
    GPIO.output(pin_i3, GPIO.HIGH)
    GPIO.output(pin_i4, GPIO.LOW)

# Turn both motors backwards
def Backwards():
    GPIO.output(pin_i1, GPIO.LOW)
    GPIO.output(pin_i2, GPIO.HIGH)
    GPIO.output(pin_i3, GPIO.LOW)
    GPIO.output(pin_i4, GPIO.HIGH)

# Message handler
def CommandCallback(commandMessage):
    command = commandMessage.data
    if command == 'forwards':
        print('Moving forwards')
        Forwards()
    elif command == 'backwards':
        print('Moving backwards')
        Backwards()
    elif command == 'left':
        print('Turning left')
        Left()
    elif command == 'right':
        print('Turning right')
        Right()
    elif command == 'stop':
        print('Stopping')
        StopMotors()
    else:
        print('Unknown command, stopping instead')
        StopMotors()

rospy.init_node('driver')

rospy.Subscriber('command', String, CommandCallback)

rospy.spin()
print('Shutting down: stopping motors')
StopMotors()
GPIO.cleanup()


