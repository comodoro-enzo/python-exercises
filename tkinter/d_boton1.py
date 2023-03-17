import tkinter as tk

root = tk.Tk()

# evento del botón: crea un label y lo empaqueta en la ventana
def handle_click():
    myLabel = tk.Label(root, text='I just clicked a button')
    myLabel.pack()

myButton = tk.Button(root, text="Click me!", padx=25, pady=5, command=handle_click, fg='red', bg='#ccc')
myButton.pack()

root.mainloop()