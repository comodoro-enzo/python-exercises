import tkinter as tk

def button_press(btn):
    global equation_text
    equation_text += btn
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(round(eval(equation_text), 6))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Error")
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")


root = tk.Tk()
root.title("Calcolatrice")
root.configure(background="#eee")
root.geometry("260x320")
root.resizable(0,0)

equation_text = ""

equation_label = tk.StringVar()

label = tk.Label(root, textvariable=equation_label, font=('consolas', 20), bg="#333", fg="#eee", anchor="e")
label.place(x=10, y=10, width=238, height=50)


# Buttons
button_7 = tk.Button(root, text="7", font=('consolas', 16), command=lambda: button_press("7"))
button_8 = tk.Button(root, text="8", font=('consolas', 16), command=lambda: button_press("8"))
button_9 = tk.Button(root, text="9", font=('consolas', 16), command=lambda: button_press("9"))

button_4 = tk.Button(root, text="4", font=('consolas', 16), command=lambda: button_press("4"))
button_5 = tk.Button(root, text="5", font=('consolas', 16), command=lambda: button_press("5"))
button_6 = tk.Button(root, text="6", font=('consolas', 16), command=lambda: button_press("6"))

button_1 = tk.Button(root, text="1", font=('consolas', 16), command=lambda: button_press("1"))
button_2 = tk.Button(root, text="2", font=('consolas', 16), command=lambda: button_press("2"))
button_3 = tk.Button(root, text="3", font=('consolas', 16), command=lambda: button_press("3"))

button_decimal = tk.Button(root, text=".", font=('consolas', 16), command=lambda: button_press("."))
button_0 = tk.Button(root, text="0", font=('consolas', 16), command=lambda: button_press("0"))
button_equal = tk.Button(root, text="=", font=('consolas', 16), command=equals)

button_delete = tk.Button(root, text="C", font=('consolas', 14), command=clear)
button_divide = tk.Button(root, text="/", font=('consolas', 14), command=lambda: button_press("/"))
button_multiply = tk.Button(root, text="*", font=('consolas', 14), command=lambda: button_press("*"))
button_substract = tk.Button(root, text="-", font=('consolas', 14), command=lambda: button_press("-"))
button_add = tk.Button(root, text="+", font=('consolas', 14), command=lambda: button_press("+"))
# End of Buttons


# Placing buttons
button_7.place(x=10, y=70, width=60, height=60)
button_8.place(x=70, y=70, width=60, height=60)
button_9.place(x=130, y=70, width=60, height=60)

button_4.place(x=10, y=130, width=60, height=60)
button_5.place(x=70, y=130, width=60, height=60)
button_6.place(x=130, y=130, width=60, height=60)

button_1.place(x=10, y=190, width=60, height=60)
button_2.place(x=70, y=190, width=60, height=60)
button_3.place(x=130, y=190, width=60, height=60)

button_decimal.place(x=10, y=250, width=60, height=60)
button_0.place(x=70, y=250, width=60, height=60)
button_equal.place(x=130, y=250, width=60, height=60)

button_delete.place(x=200, y=70, width=48, height=48)
button_divide.place(x=200, y=118, width=48, height=48)
button_multiply.place(x=200, y=166, width=48, height=48)
button_substract.place(x=200, y=214, width=48, height=48)
button_add.place(x=200, y=262, width=48, height=48)
# End of Placing buttons


root.mainloop()