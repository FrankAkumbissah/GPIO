from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
pause()