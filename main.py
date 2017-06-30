from microbit import *
import radio

def ShowPowerOn():
    display.set_pixel(0, 0, 9)
    return   

def ClearMessageBuffer():
    incoming = radio.receive()
    while incoming == 'start':
        incoming = radio.receive()
    return

def CountDown(delay):
    x=0 
    y=0
    display.show(on)
    sleep (delay)
    for y in range(5):
        for x in range(5):
            display.set_pixel(x, y, 0)
            sleep(delay)
    return

#Show I am alive
ShowPowerOn()

on = Image( "99999:"
            "99999:"
            "99999:"
            "99999:"
            "99999")
delay = 200

radio.on()

while True:
    
    if radio.receive() == 'start':
        CountDown(delay) 
        ClearMessageBuffer()
    
    #Show I am alive                
    ShowPowerOn()
    # Clear the message buffer as it is not known how many shake messages are sent.        

    if accelerometer.current_gesture() == "shake":            
        radio.send('start')
        CountDown(delay) 
        while accelerometer.current_gesture() == "shake":
            pass
        
 
        
        
 