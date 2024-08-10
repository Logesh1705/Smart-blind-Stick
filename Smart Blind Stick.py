import machine
import utime

trigger = machine.Pin(0,machine.Pin.OUT)
echo = machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)
buzzer = machine.Pin(3,machine.Pin.OUT)

while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
         send = utime.ticks_us()
       
    while echo.value() == 1:
        recieved = utime.ticks_us()
        
    duration = recieved - send
    
    distance = (duration * 0.0343)/2
    print(distance)
    utime.sleep(0.1)
    
    if distance < 100:
        buzzer.on()
        
    else:
        buzzer.off()