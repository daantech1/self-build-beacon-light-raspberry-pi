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
    # 700 ms knipperen
    end_time = time.ticks_add(time.ticks_ms(), 700)

    while time.ticks_diff(end_time, time.ticks_ms()) > 0:
        for led in leds:
            led.value(1)
        time.sleep(0.05)

        for led in leds:
            led.value(0)
        time.sleep(0.05)

    # 1 seconde uit
    for led in leds:
        led.value(0)

    time.sleep(1)