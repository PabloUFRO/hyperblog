from machine import Pin, PWM
from time import sleep

# uPython library to control motors with the H-bridge L298N and ESP32 DEBKITV1
 
#ESP32 PINOUT = https://drive.google.com/file/d/1bQJsxdrHbP_0fmOiLdE5OCmChhQcu7oR/view?usp=sharing
#H-BRIDGE PINOUT = https://drive.google.com/file/d/1--dudUWrGzpyWKEEIy7zS6vQjkBpHAVd/view?usp=sharing

#OUTPUT CONFIGURATION 

ENA=PWM(Pin(21), freq=1000, duty=0)
IN1=Pin(15, Pin.OUT, value=0)
IN2=Pin(4, Pin.OUT, value=0)
IN3=Pin(5, Pin.OUT, value=0)
IN4=Pin(18, Pin.OUT, value=0)
ENB=PWM(Pin(19), freq=1000, duty=0)

#FUNCTIONS

def go():
    ENA.duty(512)
    ENB.duty(512)
    IN1.on()
    IN2.off()
    IN3.on()
    IN4.off()
    print('To go ahead')
    sleep(12)
    stop()
    
    

def back():
    ENA.duty(512)
    ENB.duty(512)
    IN1.off()
    IN2.on()
    IN3.off()
    IN4.on()
    print('Go back')
    sleep(10)
    stop()
    

def spin_right():
    ENA.duty(512)
    ENB.duty(512)
    IN1.off()
    IN2.on()
    IN3.on()
    IN4.off()
    print('spin right')
    sleep(10)
    stop()
    

def spin_left():
    ENA.duty(512)
    ENB.duty(512)
    IN1.on()
    IN2.off()
    IN3.off()
    IN4.on()
    print('spin left')
    sleep(10)
    stop()
       
    

def stop():
    ENA.duty(512)
    ENB.duty(512)   
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()
    print('Stopped')



    #Ahora cambié mi correo al de usuario