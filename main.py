from microbit import *
import radio

def StartUpScreen():
    display.show(Image.ALL_CLOCKS, delay=100, loop=False, clear=True)
    return   

def ShowPowerOn():
    display.set_pixel(0, 0, 9)
    return   

def ClearMessageBuffer():
    while radio.receive() != None:
        pass
    return

def WaitTillShakingStops():
    while accelerometer.current_gesture() == "shake":
        pass
    return

def GetReadyToGoAgain():
    ClearMessageBuffer()
    WaitTillShakingStops()
    return
    
def CountDown(delay):
    x=0 
    y=0
    display.show(on)
    
    for y in range(5):
        for x in range(5):
            sleep(delay)
            display.set_pixel(x, y, 0)
            
    StartUpScreen()        
    return


on = Image( "99999:"
            "99999:"
            "99999:"
            "99999:"
            "99999")
            
# set the number minutes that your talk is to last for.
minutes = 1

delay = minutes * 60 * 1000 / 25

# Main code starts here

StartUpScreen()
ShowPowerOn()

radio.on()

while True:
    
    if radio.receive() == 'start':
        CountDown(delay)
        GetReadyToGoAgain()

    #Show I am alive                
    ShowPowerOn()

    if accelerometer.current_gesture() == "shake":
        send_message = True
        while accelerometer.current_gesture() == "shake":
            if radio.receive() == "start":
                send_message = False
                break
        
        if send_message:
            radio.send('start')
            
        CountDown(delay)
        GetReadyToGoAgain()
        
        
