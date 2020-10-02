#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Button, Color, Direction
from pybricks.media.ev3dev import Image, ImageFile, SoundFile
from pybricks.tools import wait, StopWatch

class Step_counter:
    def __init__(self, speed=0, distance=0, wheel_diameter=55.5, axle_track=104):
        self.speed = speed
        self.distance = distance

        self.ev3 = EV3Brick()

        self.left_motor, self.right_motor = Motor(Port.B), Motor(Port.C)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter, axle_track)

    def advance(self):
        self.robot.straight(distance * 0.8)
        self.settings(speed)
        self.robot.straight(distance * 0.2)
        self.stop()

        #reset settings
        self.settings(100)
    
    def retreave(self):
        self.settings(100, 20)
        self.robot.drive(distance * -0.1)
        self.wait(1000)
        self.stop()

        #reset settings
        self.settings(100, 0)

    def run(self):
        self.advance()
        self.retreave()


if __name__ == '__main__':
    bot = Step_counter(speed=100, distance=200)
    bot.run()