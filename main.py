import bob
import ch1
import ch9
from pybricks.tools import wait
from pybricks.parameters import Button

bob = bob.Bob()

bob.beep(500, 500)

presses = 0
while presses < 2:
    if (bob.hub.buttons.pressed()):
        presses = presses + 1
    wait(10)

if Button.LEFT in pressed:
    print("Left button was pressed")

    
    tones_left = [
        (220, 150),
        (600, 120),
        (500, 100),
        (400, 200),
    ]

    for freq, duration in tones_left:
        bob.hub.speaker.beep(freq, duration)
        wait(duration // 2) 

    if Button.LEFT in pressed:
        ch1.solve(bob)

elif Button.RIGHT in pressed:
    print("Right button was pressed")


    tones_right = [
        (250, 100), 
        (700, 120), 
        (550, 100), 
        (450, 100), 
        (300, 150), 
    ]

    for freq, duration in tones_right:
        bob.hub.speaker.beep(freq, duration)
        wait(duration // 2) 

    ch9.solve(bob)


while any(bob.hub.buttons.pressed()):
    wait(10)

bob.beep(500, 500)
