class Bob:
    def __init__(self):
        print("Init")
        # Define your robot here

    def move(self, distance):
        print("move fwd " + str(distance))

    def turnLeft(self, degree):
        print("turning left " + str(degree))

    def turnRight(self, degree):
        print("turning right " + str(degree))