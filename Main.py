import _thread
from servo import Servo
from stepmotor import mystepmotor
from machine import Pin, ADC, PWM
import time
import random

class MotorsAndSensor(object):
    def __init__(self):
        pass
  
    def step_motor_thread(self):  # stepmotor thread
        myStepMotor = mystepmotor(14, 13, 12, 11)
        myStepMotor.moveSteps(1, 96 * 64, 3000)
        time.sleep_ms(100)
            
    def servo_motor_thread(self):  # servo motor thread
        motor = Servo(pin=21)
        motor.move(60)
        time.sleep(0.005)
        motor.move(120)
        time.sleep(0.005)
        motor.move(60)
        random_sleep_time = random.randint(1, 3)
        time.sleep(random_sleep_time)

    def sensor_thread(self):  # photoresistor thread
        adc = ADC(Pin(9))
        adc.atten(ADC.ATTN_11DB)
        while True:
            analog_value = adc.read()
            print("Analog Value = ", analog_value)
            if analog_value < 40:
                print(" => Dark")
            elif analog_value < 800:
                print(" => Dim")
            elif analog_value < 2000:
                print(" => Light")
            elif analog_value < 3200:
                print(" => Bright")
            else:
                print(" => Very bright")
            time.sleep(0.5)

# Create an object of the class
my_device = MotorsAndSensor()

while True:  # main loop
    _thread.start_new_thread(my_device.step_motor_thread, ())
    _thread.start_new_thread(my_device.servo_motor_thread, ())
    _thread.start_new_thread(my_device.sensor_thread, ())
    time.sleep(1)  # sleep for a second before starting new threads

