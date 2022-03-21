import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

#Variables
button = board.digital[4]
led = board.digital[12]
led1 = board.digital[8]

Led_on = 0
button_on = 0

it = pyfirmata.util.Iterator(board)
it.start()
button.mode = pyfirmata.INPUT

while True:
    button_state = button.read()
    if button_state != button_on:
        if button_state is False:

            led.write(0)
            led1.write(0)
            Led_on += 1
            time.sleep(.05)
            print("Pulsado")
            if Led_on == 2:
                led.write(1)
                time.sleep(2)
                led.write(0)
            elif Led_on == 4:
                
                led1.write(1)
                time.sleep(2)
                led1.write(0)
                Led_on = 0

    button_on = button_state


