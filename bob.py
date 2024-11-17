from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Bob:
    hub = any
    drivebase = any

    bottom_motor_left = any
    bottom_motor_right = any
    top_motor_left = any
    top_motor_right = any
    

    def __init__(self):
        print("Init")
        # Define your robot here

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