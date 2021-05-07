from machine import Pin, PWM
from time import sleep

#DEFINICIÓN DE PINES ESP32 DEBKITV1 PARA PUENTE H
#PINOUT = https://drive.google.com/file/d/1bQJsxdrHbP_0fmOiLdE5OCmChhQcu7oR/view?usp=sharing
#H-BRIDGE = https://drive.google.com/file/d/1--dudUWrGzpyWKEEIy7zS6vQjkBpHAVd/view?usp=sharing

#Configuración interfaz IO

ENA=PWM(Pin(21), freq=1000, duty=0)
IN1=Pin(15, Pin.OUT, value=0)
IN2=Pin(4, Pin.OUT, value=0)
IN3=Pin(5, Pin.OUT, value=0)
IN4=Pin(18, Pin.OUT, value=0)
ENB=PWM(Pin(19), freq=1000, duty=0)

#funciones

def adelante():
    ENA.duty(512)
    ENB.duty(512)
    IN1.on()
    IN2.off()
    IN3.on()
    IN4.off()
    print('Hacia adelante')
    sleep(10)
    frena()
    
    

def atras():
    ENA.duty(512)
    ENB.duty(512)
    IN1.off()
    IN2.on()
    IN3.off()
    IN4.on()
    print('Hacia atras')
    sleep(10)
    frena()
    

def gir_der():
    ENA.duty(512)
    ENB.duty(512)
    IN1.off()
    IN2.on()
    IN3.on()
    IN4.off()
    print('Hacia atras')
    sleep(10)
    frena()
    

def gir_izq():
    ENA.duty(512)
    ENB.duty(512)
    IN1.on()
    IN2.off()
    IN3.off()
    IN4.on()
    print('Hacia atras')
    sleep(10)
    frena()
       
    

def frena():
    ENA.duty(512)
    ENB.duty(512)   
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()
    print('motores detenidos')



    #Ahora cambié mi correo al de usuario