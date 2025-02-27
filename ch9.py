import bob


def solve (bob):
    #moving to banana boat
    bob.forward(405)
    bob.turn(45)
    bob.forward(82)
    bob.frontmotor(-190)
    bob.reverse(230)
    
    #octopus challenge
    bob.frontmotor(190)
    bob.topmotors(-195)
    bob.turn(-80)
    
    #fetch octopus
    bob.forward(125)
    bob.reverse(155)
    #move the octopus
    bob.turn(-50)
    bob.forward(175)
    bob.turn(30)
    bob.forward(350)
    bob.turn(45)
    
#doing kraken challenge
    #bob.reverse(200)
    #bob.turn(180)
