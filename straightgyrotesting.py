import bob
def solve (bob):
    bob.imu.ready()

    # from pybricks.hubs import PrimeHub
# from pybricks.pupdevices import Motor, ColorSensor
# from pybricks.parameters import Direction, Port
# from pybricks.robotics import DriveBase
# from pybricks.tools import wait

# hub = PrimeHub()
# bottom_motor_left = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
# bottom_motor_right = Motor(Port.D)
# drivebase = DriveBase(bottom_motor_left, bottom_motor_right, 56, 143)

# hub.imu.reset_heading(0)

# target_heading = 0

# drive_speed = 897
# correction_factor = 0.2

# while True:
#     current_heading = hub.imu.heading()
#     error = current_heading - target_heading
#     turn_rate = -error * correction_factor
#     drivebase.drive(drive_speed, turn_rate)
#     wait(50)

