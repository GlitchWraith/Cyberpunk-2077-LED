import time
import random
import board
import adafruit_dotstar as dotstar

dots_len = 30
dots_lum = 0.3
# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, dots_len, brightness=dots_lum)


# Left side
bank_A_Start = 0
bank_A_End = 15
# Right side
bank_B_start = 16
bank_B_End = 30

# HELPERS
# a random color 0 -> 224
def random_color():
    return random.randrange(0, 7) * 32

def random_color_limited():
    return random.randrange(1, 14) * 15

# MAIN LOOP
n_dots = dots_len
while True:
    # Fill each dot with a random color
    for dot in range(n_dots):
        dots[dot] = (random_color(), random_color(), random_color())

    time.sleep(.25)
