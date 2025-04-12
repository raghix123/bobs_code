import bob
import ch1
import ch9
import moveboardstuff
from pybricks.parameters import Button
from pybricks.tools import wait

TONES_LEFT = [
    (220, 150),
    (400, 200),
    (500, 100),
    (600, 120)
]

TONES_RIGHT = [
    (600, 120),
    (500, 100), 
    (400, 200), 
    (220, 150)
]

TONES_MIDDLE = [
    (523, 37),
    (523, 37),
    (523, 37),
    (440, 37),
    (523, 37),
    (659, 37),
    (523, 37),
    (440, 37),
    (523, 37),
    (523, 37),
    (523, 37),
    (440, 37),
    (523, 75)
]

bob = bob.Bob()
bob.beep(250, 500)

def play_tones(tone):
    for freq, duration in tone:
        bob.hub.speaker.beep(freq, duration)
        wait(duration // 2)

def any_button_pressed():
    while True:
        if Button.LEFT in bob.hub.buttons.pressed():
            return Button.LEFT
        elif Button.RIGHT in bob.hub.buttons.pressed():
            return Button.RIGHT
        elif Button.CENTER in bob.hub.buttons.pressed():
            return Button.CENTER
        else:
            wait(10)

while True:
    button = any_button_pressed()

    if button == Button.LEFT:
        print("Left button was pressed")
        play_tones(TONES_LEFT)
        button = any_button_pressed()
        if button == Button.LEFT:
            ch1.solve(bob)

    elif button == Button.RIGHT:
        print("Right button was pressed")
        play_tones(TONES_RIGHT)
        button = any_button_pressed()
        if button == Button.RIGHT:
            ch9.solve(bob)

    elif button == Button.CENTER:
        print("Center Button was pressed")
        play_tones(TONES_MIDDLE)
        button = any_button_pressed()
        if button == Button.CENTER:
            moveboardstuff.solve(bob)
