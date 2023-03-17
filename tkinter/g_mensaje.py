import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def mostrarMensaje():
    messagebox.showinfo("Titulo", "Esto es un mensaje de info")
    # messagebox.showwarning("Titulo", "Esto es un mensaje de advertencia")
    # messagebox.showerror("Titulo", "Esto es un mensaje de error")
    
    # rta = messagebox.askquestion("Título", "Esto es una pregunta")
    # print(rta) # yes / no

btnMensaje = tk.Button(root, text="Mostrar", command=mostrarMensaje)
btnMensaje.grid(row=0, column=0)

root.mainloop()