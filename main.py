#!/usr/bin/python
#--------------------------------------
# LCD control program
#--------------------------------------
import sys
import lcd
import time
from subprocess import call

LINE_1 = 1
LINE_2 = 2
counter = 0
threshold = 12.5
seconds = 10
weight = 24

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
    isCountingDown = False
    countdownTimer = seconds
    
    while True:

        ## **** TEST
        ## ****
            
        # start the weight sensor
        # weight = 0  # shell out to C program to get reading

        if weight < threshold:
            # start LCD countdown
            #lcd.countdown(seconds,"Refill the soda!")
            print("Refill the soda!")
            isCountingDown = True
            i = 0
        else:
            weight -= 1
            if isCountingDown == True:
                countdownTimer -= 1
                isCountingDown = False
                print("Cleanup GPIO")
                #lcd.cleanupGPIO()        
        
  except KeyboardInterrupt:
    pass
  #finally:
    # lcd_byte(0x01, LCD_CMD)
    # lcd_string("Goodbye!",LCD_LINE_1)
    # GPIO.cleanup()
