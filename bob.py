from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.parameters import Axis

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
        # self.hub = PrimeHub(top_side=Axis.X, front_side=Axis.Z, broadcast_channel=0)
        self.top_motor_left = Motor(Port.E)
        self.top_motor_right = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
        self.bottom_motor_left = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
        self.bottom_motor_right = Motor(Port.D)
        self.color_sensor = ColorSensor(Port.B)
        self.front_motor = Motor(Port.A)
        self.drivebase = DriveBase(self.bottom_motor_left, self.bottom_motor_right, 56, 143)
        self.hub.speaker.volume(100)
        # self.use_gyro(True)

    # def use_gyro(self, enable):
    #     if enable:
    #         self.hub.reset_heading(0)
    #         print("Gyro enabled and set to 0 degrees")
    #     else:
    #         print("Gyro disabled")

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

    def frontmotor(self, degrees):
        print("moving front motor " + str(degrees))
        self.front_motor.run_angle(100, degrees, then=Stop.HOLD,wait=True)

    def leftmotor(self, degrees):
        print("moving lef topl motor " + str(degrees))
        self.top_motor_left.run_angle(100, degrees, then=Stop.HOLD,wait=True)

    def rightmotor(self, degrees):
        print("moving right top motor " + str(degrees))
        self.top_motor_right.run_angle(100, degrees, then=Stop.HOLD,wait=True)

    def topmotors(self, degrees):
        print("moving both top motor " + str(degrees))
        self.top_motor_right.run_angle(100, degrees, then=Stop.HOLD,wait=False)
        self.top_motor_left.run_angle(100, degrees, then=Stop.HOLD,wait=True)

    def forward_and_left_front(self, degrees, distance):
        self.top_motor_left.run_angle(100, degrees, then=Stop.HOLD,wait=False)
        self.drivebase.straight(distance,then=Stop.HOLD, wait=True)

    def imustatus(self):
        while self.imu.ready == False:
            print("Waiting for IMU")
        else:
            print("IMU is ready, starting code")