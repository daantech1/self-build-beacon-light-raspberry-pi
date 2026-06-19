from machine import Pin
import time

leds = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(6, Pin.OUT),
    Pin(7, Pin.OUT),
    Pin(8, Pin.OUT),
    Pin(9, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(11, Pin.OUT)
]

while True:
    for pos in range(12):

        # alles uit
        for led in leds:
            led.value(0)

        # hoofdlicht
        leds[pos].value(1)

        # gloed ervoor en erachter
        leds[(pos - 1) % 12].value(1)
        leds[(pos + 1) % 12].value(1)

        time.sleep(0.05)