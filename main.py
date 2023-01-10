rnd = 0

def on_gesture_shake():
    global rnd
    rnd = randint(1, 6)
    index = 0
    while index <= rnd - 1:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.QUARTER))
        index += 1
    if rnd == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif rnd == 2:
        basic.show_leds("""
            . . . . .
                        . # . . .
                        . . . . .
                        . . . # .
                        . . . . .
        """)
    elif rnd == 3:
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . #
        """)
    elif rnd == 4:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    elif rnd == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    else:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
