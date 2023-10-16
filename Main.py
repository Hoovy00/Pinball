import _thread
import time
import random
from servo import Servo
from stepmotor import mystepmotor
from machine import Pin, ADC, PWM
from time import sleep

class Music(object):

    def __init__(self):
        self.buzzer = PWM(Pin(16))
        self.tones = {
        "B0": 31,"C1": 33,"CS1": 35,"D1": 37,"DS1": 39,"E1": 41,"F1": 44,"FS1": 46,
        "G1": 49,"GS1": 52,"A1": 55,"AS1": 58,"B1": 62,"C2": 65,
        "CS2": 69,"D2": 73,"DS2": 78,"E2": 82,"F2": 87,"FS2": 93,"G2": 98,
        "GS2": 104,"A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,
        "D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,
        "G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,"C4": 262,"CS4": 277,"D4": 294,"DS4": 311,
        "E4": 330,"F4": 349,"FS4": 370,"G4": 392,"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,"C5": 523,"CS5": 554,"D5": 587,"DS5": 622,"E5": 659,"F5": 698,
        "FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,"C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1319,"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,
        "A6": 1760,"AS6": 1865,"B6": 1976,"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,
        "AS7": 3729,"B7": 3951,"C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978
    }
        self.score = ["E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "A5", "E5", "E5"]
        self.game_over = ["D4", "E4", "F4", "G4", "E4", "C4", "D4", "D4", "D4"]
        self.start = ["F5", "E5", "G4", "A4", "A4", "A4"]

    def playtone(self, frequency):
        self.buzzer.duty_u16(1000)
        self.buzzer.freq(frequency)

    def bequiet(self):
        self.buzzer.duty_u16(0)

    def playsong(self, mysong):
        for i in range(len(mysong)):
            if (mysong[i] == 0 ):
                self.bequiet()
            else:
                self.playtone(self.tones[mysong[i]])
            sleep(0.05)
        self.bequiet()

music = Music()

class Motors(object):
  
    myStepMotor = mystepmotor(14, 13, 12, 11)  # Initialize once
  
    def step_motor_thread(self):  # stepmotor thread
        while True:
            self.myStepMotor.moveSteps(1, 96 * 64, 3000)
            time.sleep_ms(100)
            
    def servo_motor_thread(self):  # servo motor thread
        motor = Servo(pin=21)  # Initialize once
        while True:
            motor.move(60)
            time.sleep(0.005)
            motor.move(120)
            time.sleep(0.005)
            motor.move(60)
            random_sleep_time = random.randint(1, 3)
            time.sleep(random_sleep_time)

class Sensor(object):

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

# Create class objects
motors = Motors()
sensor = Sensor()
music = Music()
music.playsong(music.start)

_thread.start_new_thread(motors.step_motor_thread, ())
_thread.start_new_thread(motors.servo_motor_thread, ())
