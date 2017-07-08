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

def DisplayMinutes(minutes):
    x=0 
    y=0
    i=0
    
    for y in range(5):
        for x in range(5):
            i += 1
            if (i<=minutes):
                display.set_pixel(x, y, 9)
            else: 
                display.set_pixel(x, y, 0)
                

def GetTalkTime(minutes):
    display.scroll("A -1, B +1")
    
    #clear press counters
    button_a.get_presses()
    button_b.get_presses()
    
    quit = False
        
    while quit != True:
        minutes = minutes - button_a.get_presses() + button_b.get_presses();
        DisplayMinutes(int(minutes))

        # To exit press a for 2 seconds
        if button_a.is_pressed():
            start = running_time()
        
            while button_a.is_pressed():
                if ((running_time() - start) > 2000):
                    quit = True
                    display.scroll(str(int(minutes)))
            
    return minutes       
            
def MinutesToDelay(minutes):
    return minutes * 60 * 1000 / 25

def DelayToMinutes(delay):
    return delay * 25 / (60 * 1000)


on = Image( "99999:"
            "99999:"
            "99999:"
            "99999:"
            "99999")
            
# set the number minutes that your talk is to last for.
minutes = 1

#convert to the delay needed to turn off each LED
delay = MinutesToDelay(minutes)

# Main code starts here

StartUpScreen()
ShowPowerOn()

radio.on()

while True:
    
    if radio.receive() == 'start':
        CountDown(delay)
        GetReadyToGoAgain()

    #Show number of mins                
    DisplayMinutes(DelayToMinutes(delay))
    
    # To enter demo mode press button a for > 2 secs
    if button_b.is_pressed():
        start = running_time()
        
        while button_b.is_pressed():
            pass
        
        if ((running_time() - start) > 2000):
            delay = MinutesToDelay(15/60)
            display.scroll("Talk 15 secs")
        
    if button_a.is_pressed():
        delay = MinutesToDelay(GetTalkTime(DelayToMinutes(delay)))
        StartUpScreen()
        DisplayMinutes(DelayToMinutes(delay))
 
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
        
        
