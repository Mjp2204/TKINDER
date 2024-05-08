from tkinter import Tk, Button, Entry, Label

def saludar():
    print("Hola Mundo")

root = Tk()
texto 
boton = Button(root, text="Saludar", command=saludar)
boton.pack()
boton.mainloop()