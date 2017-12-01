#!/usr/bin/python
#--------------------------------------
# LCD control program
#--------------------------------------
 
# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND
 
import RPi.GPIO as GPIO
import time
 
# Define GPIO to LCD mapping
LCD_RS = 26  # change from GPIO 7 to GPIO 21 to GPIO 26
LCD_E  = 19  # change from GPIO 8 to GPIO 20 to GPIO 19
LCD_D4 = 13  # change from GPIO 25 to GPIO 13
LCD_D5 = 6   # change from GPIO 24 to GPIO 6
LCD_D6 = 5   # change from GPIO 23 to GPIO 5
LCD_D7 = 11  # change from GPIO 18 to GPIO 11 
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

if __name__ == '__main__':
    countdown(30, "Refill the soda!")

def initGPIO():    
    # initialize GPIO pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7

def clearDisplay():
    # 000001 Clear display
    lcd_byte(0x01,LCD_CMD)

def cleanupGPIO():
    GPIO.cleanup()

def goodbye(message):
    clearDisplay()
    lcd_string(message,LCD_LINE_1)
    time.sleep(1)
    clearDisplay()

def countdown(seconds, greeting):
  try:
    initGPIO()  
    lcd_init()    

    # iterate over seconds to perform countdown
    while seconds:
      mins, secs = divmod(seconds, 60)
      formattedTime = '{:02d}:{:02d}'.format(mins, secs)

      lcd_sendText(greeting, LCD_LINE_1)
      lcd_sendText(formattedTime, LCD_LINE_2)
    
      time.sleep(1)

      seconds -= 1
      
      clearDisplay() 
      
  except KeyboardInterrupt:
    pass
  finally:
    cleanupGPIO()
 
def lcd_init():
  # initialize display
  lcd_byte(0x33,LCD_CMD) # 110011 initialize
  lcd_byte(0x32,LCD_CMD) # 110010 initialize
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def sendText(message,line,timeToDisplay):
  try:
    initGPIO()  
    lcd_init()    

    if line==1:
        lcd_sendText(message,LCD_LINE_1)
    if line==2:
        lcd_sendText(message,LCD_LINE_2)    # iterate over seconds to perform countdown
    if timeToDisplay > 0:
        time.sleep(timeToDisplay)
        clearDisplay()
      
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
 
def lcd_sendText(message,line):
  # Send string to display 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
##if __name__ == '__main__':
## 
##  try:
##    testLCD()
##  except KeyboardInterrupt:
##    pass
##  finally:
##    lcd_byte(0x01, LCD_CMD)
##    # lcd_string("Goodbye!",LCD_LINE_1)
##    GPIO.cleanup()
