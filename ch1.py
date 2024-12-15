import bob

def moveIntoPosition(bob):
    print("moving...")

def solve(bob):
    bob.forward_and_left_front(65,60)
    bob.forward(75, block=True)
    bob.leftmotor(20)
    bob.forward(40, block=True)
    bob.leftmotor(25)
    bob.forward(65, block=True)
    bob.leftmotor(-30)