from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Bob:
    hub = any
    drivebase = any
    top_motor_left = any
    top_motor_right = any
    bottom_motor_left= any
    bottom_motor_right = any
    color_sensor = any
    front_motor = any

    def __init__(self):
        hub = PrimeHub()
        top_motor_left = Motor(Port.E)
        top_motor_right = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
        bottom_motor_left = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
        bottom_motor_right = Motor(Port.D)
        color_sensor = ColorSensor(Port.B)
        front_motor = Motor(Port.A)
        drivebase = DriveBase(bottom_motor_left, bottom_motor_right, 50, 145)

    def move(self, distance):
        print("move fwd " + str(distance))
        stop_everything()
        bottom_motor_left.run(-30)
        bottom_motor_right.run(-30)
        wait(3000)

    def turnLeft(self, degree):
        print("turning left " + str(degree))

    def turnRight(self, degree):
        print("turning right " + str(degree))

    def stop_everything():
        top_motor_left.stop()
        bottom_motor_right.stop()
        bottom_motor_left.stop()
        top_motor_right.stop()