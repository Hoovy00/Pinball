from machine import ADC, Pin
import time

# Initialize ADC and the pin where the photoresistor is connected
adc = ADC(Pin(9))  # Create ADC object on GPIO pin 34
adc.atten(ADC.ATTN_11DB)  # Set attenuation for up to 3.6V

while True:
    analog_value = adc.read()  # Read analog value
    print("Analog Value = ", analog_value)

    # Interpret the analog value
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

    time.sleep(0.5)  # Wait for 500ms

