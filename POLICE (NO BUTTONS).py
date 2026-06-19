from machine import Pin
import time

left = [Pin(i, Pin.OUT) for i in range(6)]
right = [Pin(i, Pin.OUT) for i in range(6, 12)]

while True:
    for _ in range(3):
        for led in left:
            led.value(1)
        time.sleep(0.08)
        for led in left:
            led.value(0)
        time.sleep(0.08)

    for _ in range(3):
        for led in right:
            led.value(1)
        time.sleep(0.08)
        for led in right:
            led.value(0)
        time.sleep(0.08)