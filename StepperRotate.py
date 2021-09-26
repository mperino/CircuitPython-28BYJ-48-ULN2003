import time
import board
import digitalio
## Define PINS
pin1 = digitalio.DigitalInOut(board.GP0)
pin2 = digitalio.DigitalInOut(board.GP1)
pin3 = digitalio.DigitalInOut(board.GP2)
pin4 = digitalio.DigitalInOut(board.GP3)
pin1.direction = digitalio.Direction.OUTPUT
pin2.direction = digitalio.Direction.OUTPUT
pin3.direction = digitalio.Direction.OUTPUT
pin4.direction = digitalio.Direction.OUTPUT
#Define steps per rotation
stepsperrot = 2048



def statefromsteppin(pin, step):
    #   step 1 2 3 4
    # pin 1  1 1 0 0
    # pin 2  0 1 1 0
    # pin 3  0 0 1 1
    # pin 4  1 0 0 1
    #
    Offset = [1, 0, 3, 2]
    Timing = [0, 1, 1, 0]
    TPOS = ((step - 1) % 4 + Offset[pin - 1]) % 4
    if Timing[TPOS] == 1:
        return True
    else:
        return False

def rotatestepsatrpm(steps, rpm):
    if steps >= 1:
        for i in range(1, steps + 1):
            firepins(i)
            time.sleep(60 / (rpm * stepsperrot))
    if steps <= 1:
        for i in range(-1, steps - 1, -1):
            firepins(i)
            time.sleep(60 / (rpm * stepsperrot))

def firepins(nextstep):
    print("Step:{}".format(nextstep))
    pin1.value = statefromsteppin(1, nextstep)
    pin2.value = statefromsteppin(2, nextstep)
    pin3.value = statefromsteppin(3, nextstep)
    pin4.value = statefromsteppin(4, nextstep)
    
# Rotate Stepper 1 full turn in each direction, pausing 30 sec between directions
forwardRPM=4
backwardsRPM=8
rotatestepsatrpm(stepsperrot, forwardRPM)
time.sleep(30)
rotatestepsatrpm(-1 * stepsperrot, backwardsRPM)
time.sleep(30)
