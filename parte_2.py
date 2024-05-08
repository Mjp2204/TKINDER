from tkinter import Tk, Button

def saludar():
    print("Hola Mundo")

root = Tk()
boton = Button(root, text="Saludar", command=saludar)
boton.pack()
root.mainloop()