import time
import random
import board
import adafruit_dotstar as dotstar

# Function of script

Animation = 1
# 1 R B bank wave 
# 2 Solid Color
#
#
dots_len = 42
dots_lum = 0.5






# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, dots_len, brightness=dots_lum, auto_write=False)










# Left side
bank_A_Start = 0
bank_A_End = 20

#Left Top Side
bank_a_subBank1_Start = bank_A_Start
bank_a_subBank1_End =   6
#Left Middle
bank_a_subBank2_Start = 7
bank_a_subBank2_End =   13
#Left Bottom
bank_a_subBank3_Start = 14
bank_a_subBank3_End =   bank_A_End

# Right side
bank_B_start = 21
bank_B_End = 41
#Right Top
bank_b_subBank1_Start = 35
bank_b_subBank1_End =   bank_B_End
#Right Middle
bank_b_subBank2_Start = 28
bank_b_subBank2_End =   34
#Right Bottom
bank_b_subBank3_Start = bank_B_start
bank_b_subBank3_End =   27

# HELPERS
# a random color 0 -> 224
def random_color():
    return random.randrange(0, 60) * 4

def random_color_limited():
    return random.randrange(1, 14) * 15

def random_percent():
    return (random.randrange(0, 100) /100)

def random_percent_limits(low = 0,high = 100):
    return (random.randrange(low, high) /100)

def limit_check(ColorValue=250):
    if ColorValue > 240:
        return False
    else :
        return True

def color_modifi(colorValue=100, Shift_Limit=20):
    Shift = random.randrange(1,Shift_Limit)
    if  limit_check ( ( colorValue + Shift) ) == True :
        Shift = Shift * random.randrange(-1, 1)
        colorValue = abs ( colorValue + Shift)
    else :
        colorValue = abs ( colorValue - Shift)

    return colorValue
    



if Animation == 1 :
    while True: 

        # Baseline Color values
        R = random_color()
        B = random_color() 
        G = 0
        L = random_percent_limits(10,dots_lum)

        # Top row Left
        for dot in range(bank_a_subBank1_Start,bank_a_subBank1_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank1_Start,bank_b_subBank1_End):
            dots[dot] = (R , G, B, L)

        #Change values for Middle Bank
        R = color_modifi(R, 20)
        B = color_modifi(B, 40)

        for dot in range(bank_a_subBank2_Start,bank_a_subBank2_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank2_Start,bank_b_subBank2_End):
            dots[dot] = (R , G, B, L)

        R = color_modifi(R, 20)
        B = color_modifi(B, 40)

        for dot in range(bank_a_subBank3_Start,bank_a_subBank3_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank3_Start,bank_b_subBank3_End):
            dots[dot] = (R , G, B, L)

        dots.show()
        time.sleep(0.05)