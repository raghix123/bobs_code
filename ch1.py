import bob
from pybricks.tools import wait

def moveIntoPosition(bob):
    print("moving...")

def solve(bob):
    # # # # Run to Coral Tree
    bob.forward(260)

    # # # # # Solve Coral Tree
    bob.forward_and_left_front(69,60)
    bob.forward(75)
    bob.leftmotor(20)
    bob.forward(40)
    bob.leftmotor(15)
    bob.forward(65)
    bob.leftmotor(-65)

    # # # # # Reversing away from Coral Tree
    bob.reverse(100)

    # # # # # Run to Coral Buds
    bob.turn(90)
    bob.forward(300)
    bob.turn(-90)
    bob.forward(352)
    bob.turn(-90)

    # # # # # Solve Coral Buds
    bob.forward(22)
    bob.leftmotor(-33)
    bob.forward(65)
    bob.leftmotor(50)

    # # # # Solve Mr. Diddyghav(aka sharky boi)
    bob.turn(49.6)
    bob.forward(43)
    bob.leftmotor(-63)

    # #go back to spawn
    bob.leftmotor(40)
    bob.reverse(50)
    bob.turn(50)
    bob.reverse(700)
    
    # Solve Raise the mast
    bob.forward(550)
    bob.turn(95)
    bob.forward(40)
    bob.leftmotor(200)
