import tkinter as tk

root = tk.Tk()
root.title('Mi primer ventana')

myLabel = tk.Label(root, text='Bonjour')
# Metemos el label en la ventana
# en este ej. usamos pack() pero hay existen mejores maneras
# pack hace que el tamaño de la ventana se ajuste al label
myLabel.pack()

root.mainloop()