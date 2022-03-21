import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

#Variables---------------
#Variables
button = board.digital[4]
led = board.digital[12]
led1 = board.digital[8]

Led_on = 0
button_on = 0

#Iterador------------------
it = pyfirmata.util.Iterator(board)
it.start()
#-------------------------

def luz():
    on = input("Ingrese AY para encender intermitentemente").upper()
    if on == 'AY':
        while True:
            led.write(1)
            led1.write(1)
            time.sleep(.5)
            led.write(0)
            led1.write(0)
            time.sleep(.5)        
    else: 
        print("No son las Teclas correspondientes\n")

while True:
    luz()