#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [11,12,13,15]
Step2Pins = [31,33,35,37]

 
# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
for pin in Step2Pins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[0,0,0,1],
       [0,0,1,1],
       [0,0,1,0],
       [0,1,1,0],
       [0,1,0,0],
       [1,1,0,0],
       [1,0,0,0],
       [1,0,0,1]]
direct=1
cnt=0
StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
count=0 
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
  cnt = int(sys.argv[2])
  direct = int(sys.argv[3])
  StepDir=int(direct)*StepDir
  print "StepDir"
  print StepDir

else:
  WaitTime = 10/float(1000)
 
# Initialise variables
StepCounter = 0
 
# Start main loop
while True:
    while count<cnt:
      print StepCounter,
     # print Seq[StepCounter]

      for pin in range(0, 4):
          xpin = StepPins[pin]
          x2pin = Step2Pins[pin]
          if Seq[StepCounter][pin]!=0:
              GPIO.output(xpin, True)
              GPIO.output(x2pin, True)
          else:
              GPIO.output(xpin, False)
              GPIO.output(x2pin, False)

      StepCounter += StepDir

      # If we reach the end of the sequence
      # start again
      if (StepCounter>=StepCount):
        StepCounter = 0
        count=count+1
        print count
      if (StepCounter<0):
        count = count + 1
        StepCounter = StepCount+StepDir

      # Wait before moving on
      time.sleep(WaitTime)
    count=0
    StepDir=-1*StepDir
