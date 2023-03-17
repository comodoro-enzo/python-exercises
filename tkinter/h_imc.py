# IMC = m/h^2
# 30.0 obesidad
# 25.0 - 24.9 sobrepeso
# 18.5 - 24.9 normal
# <18.5 inferior a normal

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculadora IMC")
# root.geometry("300x200")

lblPeso = tk.Label(root, text="Peso en kg: ")
txtPeso = tk.Entry(root, width=10)

lblAltura = tk.Label(root, text="Altura en cm: ")
txtAltura = tk.Entry(root, width=10)

lblResult = tk.Label(root, text="", font="Helvetica 12 bold") 




def calcularIMC():

    try:
        datoPeso = float(txtPeso.get())
        datoAltura = float(txtAltura.get())/100

        if (datoPeso <= 0) or (datoAltura <= 0):
            raise ValueError

        imc = round(datoPeso / datoAltura ** 2, 1)

        lblResult.configure(text=f"Su IMC es: {imc}")


    except ValueError:
        messagebox.showerror("Error", "Verifique los datos ingresados y vuelva a intentar.")


btnCalcula = tk.Button(root, text="Calcular", command=calcularIMC)




lblPeso.grid(row=0, column=0, sticky="W")
txtPeso.grid(row=0, column=1)

lblAltura.grid(row=1, column=0, sticky="W")
txtAltura.grid(row=1, column=1)

btnCalcula.grid(row=2, columnspan=2)
lblResult.grid(row=3, columnspan=2)





# Sección info IMC
lblInfo0 = tk.Label(root, text="IMC")
lblInfo1 = tk.Label(root, text="Superior a 30.0: obesidad")
lblInfo2 = tk.Label(root, text="Entre 25.0 y 29.9: sobrepeso")
lblInfo3 = tk.Label(root, text="Entre 18.5 y 24.9: peso normal")
lblInfo4 = tk.Label(root, text="Inferior a 18.5: peso por debajo de lo normal")

lblInfo0.grid(row=4, columnspan=4, sticky="W")
lblInfo1.grid(row=5, columnspan=4, sticky="W")
lblInfo2.grid(row=6, columnspan=4, sticky="W")
lblInfo3.grid(row=7, columnspan=4, sticky="W")
lblInfo4.grid(row=8, columnspan=4, sticky="W")
# FIN de sección info IMC



root.mainloop()

