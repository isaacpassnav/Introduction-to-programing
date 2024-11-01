
import tkinter as tk
import math

# Ventana principal 
raiz = tk.Tk()
raiz.title("Calculadora cientifica")
# Entrada 

entrada = tk.Entry(raiz, width=30)
entrada.grid(row=0, column=0, columnspan=4)
#Etiqueta para mostrar resultado

etiqueta_resultado = tk.Label(raiz, text="Resultado: ")
etiqueta_resultado.grid(row=1, column=0, columnspan=4)

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        etiqueta_resultado.config(text = "Resultado: " + str(resultado))
    except Exception as e:
        etiqueta_resultado.config(text="Error")

def click_en_boton(valor):
    entrada.insert(tk.END, valor)



# Botones de Digitos y operadores

botones = [
    ("7", 7), ("8", 8), ("9", 9), ("+"),
    ("4", 4), ("5", 5), ("6", 6), ("-"),
    ("1", 1), ("2", 2), ("3", 3), ("*"),
    ("0", 0), (".", "."), ("/"), 
    ("π", "math.pi"), 

]

fila = 2 
columna = 0

for texto_boton, valor in botones:
    tk.Button(raiz, text=texto_boton, width=6, command=lambda v=texto_boton: click_en_boton(v)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
# Boton de igual 

tk.Button(raiz, text = "=", width=6, command=calcular).grid(row=fila, column=0, columnspan=4)
# Ejecutra la aplicacion

raiz.mainloop()
