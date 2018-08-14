## test file for testing things
import time
from gpiozero import LED, LineSensor
from signal import pause
pump = LED(2)
water = LineSensor(23)
water_indicator = LED(24)

def on():
    pump.on()

def off():
    pump.off()

def wet():
    print("wet")
    water_indicator.on()

def dry():
    print("dry")
    water_indicator.off()

water.when_line = dry
water.when_no_line = wet

off()
pause()

