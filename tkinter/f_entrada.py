import tkinter as tk

root = tk.Tk()
root.geometry("250x250")

lblNombre = tk.Label(root, text="Nombre:")
lblNombre.grid(row=0, column=0)

txtNombre = tk.Entry(root, width=12)
txtNombre.grid(row=0, column=1)

def accionSaludar():
    datoEntrada = txtNombre.get()
    lblNombre.configure(text=datoEntrada)

btnNombre = tk.Button(root, text='Saluda', command=accionSaludar)
btnNombre.grid(row=0, column=2)

root.mainloop()