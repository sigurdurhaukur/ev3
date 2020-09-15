#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for one meter.
print("Push Challenge")

def y_axis(millimeters=0, speed=100):
    Drive_speed = speed
    print("forward {millimeters}")
    robot.straight(millimeters)
    ev3.speaker.beep()

def x_axis(degrees=0):
    print("turning {degrees}degrees")
    robot.turn(degrees)

# y_axis(500, 200)
ev3.speaker.beep()
