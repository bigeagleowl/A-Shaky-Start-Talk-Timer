from microbit import *
import radio

#A Staky Start Talk Time
shakyId = "asstt" 

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
            if AbandonTalk() == True:
                return
            
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

def MessageToDelay(receivedmess):
    if receivedmess is not None:
        asstdev, started, remotetime = receivedmess.split()
        
        if asstdev == shakyId and started == "start":
            return float(remotetime)
        
    return -1
    
def AbandonTalk():
    if button_a.is_pressed():
        radio.send(shakyId + " " + "stop")
        display.show(Image.SKULL)
        while button_a.is_pressed():
            pass
        return True
        
    receivedmess = radio.receive()
    if receivedmess is not None:
        asstdev, stopped = receivedmess.split()
        
        if asstdev == shakyId and stopped == "stop":
            return True
        
    return False    
    

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
    
    receivedmess = radio.receive()
    
    delayFromRemote = MessageToDelay(receivedmess)
    
    if delayFromRemote >= 0:
        delay = delayFromRemote
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
            delayFromRemote = MessageToDelay(receivedmess)
            if delayFromRemote >= 0:
                delay = delayFromRemote
                send_message = False

        if send_message:
            radio.send(shakyId + " " + "start " + str(delay))
            
            
        CountDown(delay)
        GetReadyToGoAgain()
        
        