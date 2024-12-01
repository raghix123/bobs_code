import bob
import ch1
import ch2

bob = bob.Bob()

bob.beep(250, 500)

# 50 mm fwd
bob.forward(50)
# 100 mm back
bob.reverse(100)
# turn 90d left
bob.turn(-90)
# turn 70d right
bob.turn(70)
# move front motor 20d

bob.beep(500, 500)

# ch1.moveIntoPosition(bob)
# ch1.solve(bob)

# ch2.moveIntoPosition(bob)
# ch2.solve(bob)