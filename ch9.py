import bob


def solve (bob):
    #moving to banana boat
    bob.turn(1)
    bob.forward(405)
    bob.turn(45)
    bob.forward(85)
    bob.frontmotor(-190)
    bob.reverse(300)

    #octopus challenge
    bob.frontmotor(190)
    bob.topmotors(-195)
    bob.turn(-80)
    #fetch octopus
    bob.forward(125)
    bob.reverse(155)

    #move the octopus
    bob.turn(-50)
    bob.forward(200)
    bob.turn(35)
    bob.forward(300)
    bob.turn(50)
    bob.forward(30)
#doing kraken challenge
    #bob.reverse(200)
    #bob.turn(180)
