#!/usr/bin/python
#--------------------------------------
# LCD control program
#--------------------------------------
import sys
import lcd
from subprocess import call

LINE_1 = 1
LINE_2 = 2

# shell out to C program and grab the return value
return_code = call("./dummyApp", shell=True)
print return_code

# calling the function to initialize the LCD
##lcd.countdown(5, "Refill the soda!")
##
##timeToDisplay=5
##lcd.sendText("Shame on you!",LINE_1,timeToDisplay)
