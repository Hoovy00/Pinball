import _thread
from servo import Servo
from stepmotor import mystepmotor
from machine import Pin, PWM
import time
import random

def step_motor_thread(): #stepmotor thread
    myStepMotor = mystepmotor(14,13,12,11)
    while True: #while active make the motor spin
        myStepMotor.moveSteps(1,96*64,3000)
        time.sleep_ms(100)
        
def servo_motor_thread():  # servo motor thread
    motor = Servo(pin=21)
    while True:  # while active move the servo at random intervals
        motor.move(60)
        time.sleep(0.005)
        motor.move(120)
        time.sleep(0.005)
        motor.move(60)

        # Generate a random sleep time between 1 and 3 seconds
        random_sleep_time = random.randint(1, 3)

        time.sleep(random_sleep_time)
        
#Create threads
_thread.start_new_thread(step_motor_thread, ())
_thread.start_new_thread(servo_motor_thread, ())
