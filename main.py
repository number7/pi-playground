#!/usr/bin/python
#--------------------------------------
# LCD control program
#--------------------------------------
import sys
import lcd
import time
from subprocess import call
from subprocess import Popen, PIPE

LINE_1 = 1
LINE_2 = 2

# shell out to C program and grab the return value
#return_code = call("./dummyApp", shell=True)
#print return_code

# calling the function to initialize the LCD
##lcd.countdown(5, "Refill the soda!")
##
##timeToDisplay=5
##lcd.sendText("Shame on you!",LINE_1,timeToDisplay)

if __name__ == '__main__':
 
  try:
      hasCountdownCommenced = False
      hasPhotoBeenSent = False
      timeAtOffense = 0
      countdownProcess = null

      while True:

          if isWeightBelowThreshold():
              print("weight is below threshold")
              if hasCountdownCommenced:
                  if isCountdownComplete():
                      if not hasPhotoBeenSent:
                          print("tweeting photo")
                         tweetPhoto(timeAtOffense)
              else:
                  timeAtOffense = getCurrentTime()
                  print("time at offense = " + timeAtOffense)
                  print("commencing countdown")
                  countdownProcess = commenceCountdown()
                  hasCountdownCommenced = True
          else:
              print("weight is above threshold")
              hasPhotoBeenSent = False
              if hasCountdownCommenced:
                  print("stopping countdown")
                  stopCountdown()
                  countdownProcess = None
                  hasCountdownCommenced = False
  finally:

def isWeightBelowThreshold():
    weightOf12Cans = 90000
    weightOf13Cans = 100000
    weightThreshold = (weightOf12Cans + weightOf13Cans) / 2
    currentWeight = getCurrentWeight()
    return currentWeight < weightThreshold

def getCurrentWeight():
    print("getting current weight")
    return call("./hx711/hx711", shell=True) #TODO------not getting back valid weight value

def isCountdownComplete():
    return countdownProcess.poll() == None

def getCurrentTime():
    return datetime.datetime.time(datetime.datetime.now())

def commenceCountdown():
    return Popen(["python","lcd.py"], stdout=PIPE)

def stopCountdown():
    countdownProcess.terminate()

def tweetPhoto(timeAtOffense):
    theTime = timeAtOffense
    numberOfTries = 0
    while numberOfTries <= 60:
        filename = getFilename(theTime)
        if os.path.isfile(filename):
            tweetpic.GlennTBD(filename) #TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return
        else:
            theTime = decrementTime(theTime)
            numberOfTries += 1
    return

def decrementTime(theTime)
    return theTime - datetime.timedelta(seconds = 1)

def getFilename(theTime):
    "images/" + theTime.strftime("%H%M%S") + ".jpg"