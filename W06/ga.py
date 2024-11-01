import math
import tkinter as tk

nombre = input("Enter you name: ")
print("Wellcome: " + nombre)
def add(a,b):
    return a+b
def subtrack(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: cannot divide by 0"
    
def square_root(a):
    return math.sqrt(a)
def power(a,b):
    return math.pow(a,b)

def on_button_click(number):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current + str(number))

def on_cleark_click():
    entry.delete(0,tk.END)

def on_equal_click():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
# crear ventana principal

root = tk.Tk()
root.title("Scientific Calculator")
# Crear botones

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("/", 4, 3),
    ("√", 5, 0), ("^", 5, 1), ("C", 5, 2), ("(", 5, 3),
    (")", 6, 0)
]

for button_info in buttons:
    button_text, row, col = button_info
    button = tk.Button(root, text=button_text, width=5, font=("Arial", 20), command=lambda text=button_text: on_button_click(text))
    button.grid(row=row, column=col)
# Boton clear

clear_button = tk.Button(root, text="Clear", width=10, font=("Arial", 20), command=on_cleark_click)
clear_button.grid(row=6, column=3)

root.mainloop()
