"""
import getpass
account = input ("Enter your account: ")
password = getpass.getpass("Enter your password: ")

# Mostrar asteriscos en lugar de la contraseña:
password_length = len(password)
hidden_password = "*" * password_length

# pra suma 
def suma(a,b):
    return a+b
#pra resta
def resta(a,b):
    return(a-b)
# para multiplicar
def multi(a,b):
    return(a*b)
# para division
def div(a,b):
    if b !=0:
        return a/b
    else:
        print("Error, no se puede dividir entre cero.")
        return None
# Menu de opciones
def mostar_menu():
    print("calculadora")
    print("1. suma ")
    print("2. resta")
    print("3. multiplicaciòn")
    print("4. division")
    print("5. salir")
#Loop principal del programa:
while True:
    mostar_menu()
    opcion = input("Selecciona una opcion (1-5): ")

    if opcion == "1":
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        resultado = suma(numero1,numero2)
        print("El resultado de la suma es:", resultado)
    elif opcion == "2":
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        resultado = resta(numero1,numero2)
        print("El resultado es: ", resultado)
    elif opcion =="3":
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        resultado = multi(numero1,numero2)
        print("El resultado es: ", resultado)
    elif opcion == "4":
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        resultado = div(numero1, numero2)
        if resultado is not None:
            print("El resultado es: ", resultado)
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("Seleccione una funcion valida (1-5).") """

from tkinter import Tk, Button, Entry

def button_click(number):
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert('end', current + str(number))

def button_clear():
    entry.delete(0, 'end')

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, 'end')
        entry.insert('end', str(result))
    except:
        entry.delete(0, 'end')
        entry.insert('end', 'Error')

root = Tk()
root.title("Calculator")

entry = Entry(root, width=30, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Definir los botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Funciones para los botones
def create_button(button_text, button_row, button_col):
    return Button(root, text=button_text, width=10, command=lambda: button_click(button_text))

def create_operator_button(button_text, button_row, button_col):
    return Button(root, text=button_text, width=10, command=lambda: button_click(button_text))

# Crear los botones en la interfaz
row = 1
col = 0
for button in buttons:
    if button in ['/', '*', '-', '+']:
        btn = create_operator_button(button, row, col)
    elif button == '=':
        btn = Button(root, text=button, width=10, command=button_equal)
    elif button == 'C':
        btn = Button(root, text=button, width=10, command=button_clear)
    else:
        btn = create_button(button, row, col)
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
