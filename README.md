# halloweenpi

scare the neighbours kids using a Raspberry Pi, 4 * 4 keypad and some mp3s

Use the keypad and map 16 mp3s to each keypress.  The sounds will be played over a bluetooth speaker hidden in the trees

Wire the inpouts for the 4 * 4 keypad to the PINs defined in the _ROW_PINS_ and _COL_PINS_ variables

## Pair a bluetooth speaker with the RaspberryPi

ssh to the pi
Try following commands
  
  ``` 
  bluetoothctl -a
  scan on 
  ```

Find the MAC address of the speaker
  
  ```
  scan off
  pair <MAC Address>
  trust <MAC Address>
  connect <MAC Address>
  quit
  ```
  
Speaker should now be paired
  
