import tkinter as tk

root = tk.Tk()

myLabel1 = tk.Label(root, text="My name's Enzo")
myLabel2 = tk.Label(root, text="Je m'appelle Enzo")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()

# También es posible, pero no recomendable, la siguiente línea:
# myLabel = Label(root, text='hola').grid(row=0, column=1)