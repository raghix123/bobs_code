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
        self.hub = PrimeHub()
        self.top_motor_left = Motor(Port.E)
        self.top_motor_right = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
        self.bottom_motor_left = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
        self.bottom_motor_right = Motor(Port.D)
        self.color_sensor = ColorSensor(Port.B)
        self.front_motor = Motor(Port.A)
        self.drivebase = DriveBase(self.bottom_motor_left, self.bottom_motor_right, 56, 143)
        self.hub.speaker.volume(100)

    def forward(self, distance):
        print("move fwd " + str(distance))
        self.drivebase.straight(distance,then=Stop.HOLD,wait=True)

    def reverse(self, distance):
        print("move bwd " + str(distance))
        self.drivebase.straight(-1*distance,then=Stop.HOLD,wait=True)

    def turn(self, degree):
        print("turning left " + str(degree))
        self.drivebase.turn(degree,then=Stop.HOLD,wait=True)


    def stop_everything(self):
        self.top_motor_left.stop()
        self.bottom_motor_right.stop()
        self.bottom_motor_left.stop()
        self.top_motor_right.stop()

    def beep(self,frequency, time):
        self.hub.speaker.beep(frequency, time)

    def front(self, degrees):
        print("moving front motor " + str(degrees))
        self.front_motor.run_time(100, 1000*degrees/100, then=Stop.HOLD,wait=True)