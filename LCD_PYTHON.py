import sys 
sys.path.append('/usr/local/lib/python3.7/dist-packages/RPLCD')
from RPLCD import CharLCD

import RPi.GPIO as GPIO

import time
from time import sleep
import Speech_Recognition_Test  #import voice rec code
from Speech_Recognition_Test import listening

lcd = CharLCD(cols = 16, rows = 2, pin_rs = 7, pin_e = 8, pins_data = [25,24,23,18],numbering_mode=GPIO.BCM)

lcd.clear()
lcd.write_string(u'Speak Now!')
sleep(1)
while True:
    phrase = listening()
    #type on lcd what's being said
    #print(type(phrase))
    #print(len(phrase))
    lcd.clear()
    sleep(0.01)
    lcd.write_string(str(phrase))
    sleep(1) # 2 second delay
    if 'stop' in phrase:
        break
    sleep(1)
