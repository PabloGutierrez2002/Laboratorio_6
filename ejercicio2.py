from tkinter import *
root = Tk()
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

#Variables-----
button = board.digital[4]
led = board.digital[12]
led1 = board.digital[8]

Led_on = 0
button_on = 0

#Iterador--------
it = pyfirmata.util.Iterator(board)
it.start()
#---------------

def botton():
    botton1 = True
    button_state = botton1
    texto = Label(root, text="Led Apagado", bg="red",padx=100).grid()
    if button_state != button_on:
        if button_state is True:
            led.write(1)
            time.sleep(1)
            led.write(0)

botton1 = Button(root,text="Enciende Led", bg="green",padx=100, pady=25,command=botton).grid(row=0, column=0)

root.mainloop()