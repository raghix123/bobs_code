import bob
from pybricks.tools import wait

def moveIntoPosition(bob):
    print("moving...")

def solve(bob):
    bob.stopbuttonc()
    # # # # Run to Coral Tree
    bob.forward(261)

    # # # # # Solve Coral Tree
    bob.forward_and_left_front(75,60)
    bob.forward(75)
    bob.leftmotor(20)
    bob.forward(45)
    bob.leftmotor(25)
    bob.forward(65)
    bob.leftmotor(-80)

    # # # # # Reversing away from Coral Tree
    bob.reverse(70)

    # # # # # Run to Coral Buds
    bob.turn(90)
    bob.forward(295)
    bob.turn(-90)
    bob.forward(306)
    bob.turn(-88)

    # # # Solve Coral Buds
    bob.leftmotor(-40,999999)
    bob.forward(64)
    bob.leftmotor(50)

    # # # # Solve Mr. Diddyghav(aka sharky boi)
    bob.turn(50)
    bob.forward(19)
    bob.leftmotor(-69,9999999)
    bob.leftmotor(70)

    # # # # # Send over the submersible
    #go back to spawn
    # bob.leftmotor(40)
    # bob.reverse(50)
    # bob.turn(55)
    # bob.reverse(700)

    bob.stopbuttonn()
    
    # Solve Raise the mast
    # bob.forward(550)
    # bob.turn(95)
    # bob.forward(40)
    # bob.leftmotor(200)
