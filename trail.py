from gpiozero import LED, Button

red = LED(25)

button = Button(21)

while True:
    if button.is_pressed:
        red.on()
    else:
        red.off()