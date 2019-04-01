#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[0, 0, 0, 1],
       [0, 0, 1, 1],
       [0, 0, 1, 0],
       [0, 1, 1, 0],
       [0, 1, 0, 0],
       [1, 1, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 1]]

count = 0
StepPins = [31, 33, 35, 37]
direct = 1
cnt = 0
StepCount = len(Seq)
# Set to 1 or 2 for clockwise # Set to -1 or -2 for anti-clockwise
StepDir = 1


def setup():
    global StepPins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    #GPIO.cleanup()
    for pin in StepPins:
        print " stepper2  Setup pins"
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)


# Read wait time from command line
def move(timeStep=0, param_count=10, param_direct=1):
    global cnt, StepDir, count
    cnt = int(param_count)
    direct = int(param_direct)
    StepDir = int(direct) * StepDir
    print "StepDir"
    print StepDir

    if timeStep > 0:
        WaitTime = int(timeStep) / float(1000)
    else:
        WaitTime = 10 / float(1000)

    # Initialise variables
    StepCounter = 0

    # Start main loop
    while count < cnt:
        print StepCounter,
        # print Seq[StepCounter]

        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin] != 0:
                print " Enable GPIO %i" %(xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += StepDir

        # If we reach the end of the sequence
        # start again
        if (StepCounter >= StepCount):
            StepCounter = 0
            count = count + 1
            print count
        if (StepCounter < 0):
            count = count + 1
            StepCounter = StepCount + StepDir

        # Wait before moving on
        time.sleep(WaitTime)
