import bob
import ch1
import ch2

bob = bob.Bob()

bob.beep(250, 500)
print("Initialized: Starting now")

ch1.solve(bob)

ch2.solve(bob)

# fetch 1st one
bob.turn(-6)
bob.forward(360)
bob.topmotors(-100)

#fetch 1st krill 
bob.forward (50)
bob.turn(60)
bob.turn(-50)
bob.forward(58)
bob.topmotors(100)
bob.forward (30)
bob.topmotors(-100)
#bob.reverse(550)
# e(500)

#fetch 2nd krill
bob.turn(-20)
bob.forward(72)
bob.topmotors(100)
bob.forward(55)
bob.topmotors(-100)

#come back to position
bob.reverse(600)

#bob.turn(-80)
bob.beep(500, 500)


print("Program has ended")