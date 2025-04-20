import bob

def solve (bob):
    bob.stopbuttonc()
    #moving to banana boat
    bob.forward(405)
    bob.turn(45)
    bob.forward(82)
    bob.frontmotor(-190)
    bob.reverse(230)
    
    #octopus challenge
    bob.frontmotor(190)
    bob.topmotors(-195)
    bob.turn(-90)
    
    #fetch octopus
    bob.forward(125)
    bob.reverse(155)
    #move the octopus
    bob.turn(-50)
    bob.forward(175)
    bob.turn(45)
    bob.forward(350)
    bob.turn(45)
    bob.forward(50)
    bob.topmotors(195)
    bob.turn(-15)
    
    #going to and doing angler fish
    bob.reverse(100)
    bob.turn(-30)
    bob.topmotors(-195)
    bob.forward(200)
    bob.turn(-15)
    bob.forward(55)

    #return to spawn
    bob.turn(10)
    bob.reverse(900)
    bob.stopbuttonn()
    exit()