from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Bob:
    hub = any
    top_motor_left = any
    top_motor_right = any
    bottom_motor_left = any
    bottom_motor_right = any
    color_sensor = any
    front_motor = any
    drivebase = any
    speed = any

hub = PrimeHub()
top_motor_left = Motor(Port.E)
top_motor_right = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
bottom_motor_left = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
bottom_motor_right = Motor(Port.D)
color_sensor = ColorSensor(Port.B)
front_motor = Motor(Port.A)
drivebase = DriveBase(bottom_motor_left, bottom_motor_right, 50, 145)
speed = 300

def forward(distance, speed):
    bottom_motor_left.run(22.55 * speed)
    bottom_motor_right.run(22.55 * speed)
    wait(1000*distance/speed)
    stopall()

def turnleft(time, distance):
    bottom_motor_left.run(-1*distance)
    bottom_motor_right.run(distance)
    wait(time
         )

def turnright(time, distance):
    bottom_motor_left.run(distance)
    bottom_motor_right.run(-1*distance)
    wait(time)
    stopall()

def reverse(distance, speed):
    bottom_motor_left.run(-22.55 * speed)
    bottom_motor_right.run(-22.55 * speed)
    wait(1000*distance/speed)
    stopall()

def stopall():
    bottom_motor_left.stop()
    bottom_motor_right.stop()
    front_motor.stop()
    top_motor_left.stop()
    top_motor_right.stop()