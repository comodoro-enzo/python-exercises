import tkinter as tk

root = tk.Tk()
root.title("Mi ventana")
root.geometry("250x250")

# Evento
def saludar():
    lblNombre.configure(text="Hola Enzo")

# Botón
btnSaludar = tk.Button(root, text="Saluda", command=saludar)
btnSaludar.grid(column=1, row=0)

# Label
lblNombre = tk.Label(root, text="Hola")
lblNombre.grid(column=0, row=0)


root.mainloop()