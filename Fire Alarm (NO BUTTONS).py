from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in range(12)]

while True:
    for _ in range(8):
        for led in leds:
            led.value(1)
        time.sleep(0.03)

        for led in leds:
            led.value(0)
        time.sleep(0.03)

    time.sleep(0.5)