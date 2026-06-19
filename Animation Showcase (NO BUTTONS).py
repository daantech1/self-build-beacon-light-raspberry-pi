from machine import Pin
import time

leds = [
    Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT),
    Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT),
    Pin(6, Pin.OUT), Pin(7, Pin.OUT), Pin(8, Pin.OUT),
    Pin(9, Pin.OUT), Pin(10, Pin.OUT), Pin(11, Pin.OUT)
]

def alles_uit():
    for led in leds:
        led.value(0)

def alles_aan():
    for led in leds:
        led.value(1)

def looplicht():
    for i in range(12):
        alles_uit()
        leds[i].value(1)
        time.sleep(0.06)

def scanner():
    for i in range(12):
        alles_uit()
        leds[i].value(1)
        time.sleep(0.04)

    for i in range(10, 0, -1):
        alles_uit()
        leds[i].value(1)
        time.sleep(0.04)

def dubbel_looplicht():
    for i in range(12):
        alles_uit()
        leds[i].value(1)
        leds[(i + 6) % 12].value(1)
        time.sleep(0.06)

def vullen():
    alles_uit()
    for i in range(12):
        leds[i].value(1)
        time.sleep(0.05)

def om_en_om():
    for _ in range(8):
        for i in range(12):
            leds[i].value(i % 2)
        time.sleep(0.15)

        for i in range(12):
            leds[i].value((i + 1) % 2)
        time.sleep(0.15)

def burst():
    for _ in range(4):
        alles_aan()
        time.sleep(0.05)
        alles_uit()
        time.sleep(0.05)
    time.sleep(0.4)

while True:
    looplicht()
    scanner()
    dubbel_looplicht()
    vullen()
    time.sleep(0.2)
    alles_uit()
    time.sleep(0.2)
    om_en_om()
    burst()