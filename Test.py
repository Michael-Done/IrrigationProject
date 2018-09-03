## test file for testing things
from time import sleep
from gpiozero import LED, LineSensor
from signal import pause
pump = LED(4)
valve_1 = LED(2)
valve_2 = LED(3)

water = LineSensor(23)

valve_1.off()
valve_2.off()
pump.off()

def pumpOn():
    pump.on()

def pumpOff():
    pump.off()

def wet():
    print("wet")
    water_indicator.on()

def dry():
    print("dry")
    water_indicator.off()

##water.when_line = dry
##water.when_no_line = wet

pumpOff()
valve_1.off()
valve_2.off()


