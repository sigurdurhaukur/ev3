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
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

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

class Line_follow:
    def __init__(self, duration=0, wheel_diameter=55.5, axle_track=104):
        self.duration = duration
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

        self.ev3 = EV3Brick()

        self.left_motor, self.right_motor = Motor(Port.B), Motor(Port.C)
        self.line_sensor = ColorSensor(Port.S3)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter, axle_track)

    def follow(self):

        motor_speedlog = DataLog('error', 'integral', 'derivative', 'turn_rate', name='motor_speedlog', timestamp=True, extension='txt')
        black = 3
        white = 62
        threshold = (black + white) / 2
        DRIVE_SPEED = 200

        PROPORTIONAL_GAIN = 4.2
        INTEGRAL_GAIN = 0.008
        DERIVATIVE_GAIN = 0.01
        integral = 0
        derivative = 0
        last_error = 0

        while True:
            error = line_sensor.reflection() - threshold
            integral = integral + error
            derivative = error - last_error

            turn_rate = PROPORTIONAL_GAIN * error + INTEGRAL_GAIN + DERIVATIVE_GAIN + integral + DERIVATIVE_GAIN * derivative
            motor_speedlog.log(error, integral, derivative, turn_rate)

            self.left_motor.run(DRIVE_SPEED + turn_rate)
            self.right_motor.run(DRIVE_SPEED - turn_rate)

            last_error = error
            wait(10)
    def run(self):
        self.follow()

if __name__ == '__main__':
    bot = Line_follow()
    bot.run()

    bot = Step_counter(speed=100, distance=200)
    bot.run()