import bob

def moveIntoPosition(bob):
    print("moving...")

def solve(bob):
    # # Run to Coral Tree
    bob.forward(260)

    # # Solve Coral Tree
    bob.forward_and_left_front(69,60)
    bob.forward(75)
    bob.leftmotor(20)
    bob.forward(40)
    bob.leftmotor(15)
    bob.forward(65)
    bob.leftmotor(-65)

    # # Reversing away from Coral Tree
    bob.reverse(100)

    # # Run to Coral Buds
    bob.turn(90)
    bob.forward(300)
    bob.turn(-90)
    bob.forward(330)
    bob.turn(-90)

    # # Solve Coral Buds
    bob.forward(27)
    bob.leftmotor(-30)
    bob.forward(55)
    bob.leftmotor(50)

    # Solve Mr. Raghav(aka sharky boi)
    bob.turn(55)
    bob.forward(30)
    bob.leftmotor(-70)
    
    # Solve Scuba boi
    bob.leftmotor(39)
    bob.turn(-25)
    bob.forward(100)
    bob.leftmotor(25)
    bob.turn(205)
    bob.forward(200)
    bob.turn(-80)
    bob.reverse(50)
    bob.forward(60)
    bob.turn(10)
    bob.leftmotor(-50)