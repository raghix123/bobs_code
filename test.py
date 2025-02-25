import bob

def test(bob):
    pressed = []
    while not any(pressed):
        pressed = bob.hub.buttons.pressed()
        wait(10)

    if bob.Button.LEFT in pressed:
        print("Left button was pressed")
    elif bob.Button.RIGHT in pressed:
        print("Right button was pressed")


    while any(bob.hub.buttons.pressed()):
       wait(10)

test()