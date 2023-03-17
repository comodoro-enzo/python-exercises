import tkinter as tk
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.configure(text=time_string)

    day_string = strftime("%A %d")
    day_label.configure(text=day_string)

    root.after(1000, update)


root = tk.Tk()

time_label = tk.Label(root, font=("Arial", 50), fg="red", bg="black")
time_label.pack()

day_label = tk.Label(root, font=("Ink Free", 25))
day_label.pack()

update()

root.mainloop()