import bob

 # fetch 1st krill
def solve(bob):
    bob.turn(-6)
    bob.turn(-6)
    bob.forward(360)
    bob.topmotors(-100)

    #fetch green coral
    bob.forward (50)
    bob.turn(60)
    #bob.turn(-50)
    #bob.forward(58)
    bob.topmotors(100)
    bob.forward (65)
    bob.topmotors(-100)
    #bob.reverse(550)
    #bob.reverse(500)

    #fetch 2nd krill
    bob.turn(-70)
    bob.turn(20)
    bob.topmotors(100)
    bob.forward(80)
    bob.topmotors(-100)

    #come back to position
    #bob.reverse(600)
