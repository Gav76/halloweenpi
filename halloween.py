from pad4pi import rpi_gpio
import os
import time

# Setup Keypad
KEYPAD = [
        ["1","2","3","4"],
        ["5","6","7","8"],
        ["9","10","11","12"],
        ["13","14","15","16"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
ROW_PINS = [4, 14, 15, 17] # BCM numbering
COL_PINS = [18, 27, 22, 23] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_4_by_4_keypad

#keypad.cleanup()

def printKey(key):
  print(key)
  os.system('mpg123 -q ' + key + '.mp3')

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()
