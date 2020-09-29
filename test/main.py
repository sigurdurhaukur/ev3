#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

m_left= Motor(Port.B)
m_right = Motor(Port.C)

robot = DriveBase(m_left, m_right, wheel_diameter=55.5, axle_track=104)

time = 20000
robot.drive(1000, 0)
wait(time)
robot.drive(100000000000000000000, 0)
wait(time)


ev3.speaker.beep()
