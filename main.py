import bob
import ch1
import ch2
import collect_objects

bob = bob.Bob()

bob.beep(250, 500)
print("Initialized: Starting now")

ch1.solve(bob)

ch2.solve(bob)

collect_objects.solve(bob)

bob.beep(500, 500)
print("Program has ended")