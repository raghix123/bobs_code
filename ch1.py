import bob

def moveIntoPosition(bob):
    print("moving...")

def solve(bob):
    # # # Run to Coral Tree
    bob.forward(260)

    # # # Solve Coral Tree
    bob.forward_and_left_front(69,60)
    bob.forward(75)
    bob.leftmotor(20)
    bob.forward(40)
    bob.leftmotor(15)
    bob.forward(65)
    bob.leftmotor(-65)

    # # # Reversing away from Coral Tree
    bob.reverse(100)

    # # # Run to Coral Buds
    bob.turn(90)
    bob.forward(300)
    bob.turn(-90)
    bob.forward(330)
    bob.turn(-90)

    # # # Solve Coral Buds
    bob.forward(19)
    bob.leftmotor(-30)
    bob.forward(55)
    bob.leftmotor(50)

    # # Solve Mr. Raghav(aka sharky boi)
    bob.turn(54)
    bob.forward(50)
    
    # Solve Raise the mast
    # bob.reverse(100)
    # bob.turn(52.5)
    # bob.reverse(100)