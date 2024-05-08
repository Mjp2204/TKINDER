from tkinter import Tk, Button, Entry

def saludar():
    print("Hola Mundo")

root = Tk()
texto = Entry(root)
texto.pack()
boton = Button(root, text="Saludar", command=saludar)
boton.pack()
root.mainloop()