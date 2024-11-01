import math
from tkinter import *
from tkinter import ttk

def temaOscuro(*args):
    estilos.configure('mainframe.Tframe', background="#010924")

    estilos_label1.configure('Label1.TLabel', background="#010924", foreground="white")
    estilos_label2.configure('Label2.TLabel', background="#010924", foreground="white")

    estilo_botones_numeros.configure('Botonones_numeros.TButton', background="#00044A", foreground="white")
    estilo_botones_numeros.map('Botonones_numeros.TButton', background=[('active','#020A90')])

    estilo_botones_borrar.configure('Botones_borrar.TButton', background="#010924", foreground="white")
    estilo_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#000AB1')])

    estilo_botones_restantes.configure('Botones_restantes.TButton', background="010924", foreground="white")

def temaClaro(*args):
    estilos.configure('mainframe.Tframe', background="#DBDBDB", foreground="black")

    estilos_label1.configure('Label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('Label2.TLabel', background="#DBDBDB", foreground="black")

    estilo_botones_numeros.configure('Botonones_numeros.TButton', background="#FFFFFF", foreground="black")
    estilo_botones_numeros.map('Botonones_numeros.TButton',backgorund=[('active', '#B9B9B9',)])
    estilo_botones_borrar.configure('Botones_borrar.TButton', background="#CECECE", foreground="black")
    estilo_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#858585')])
    estilo_botones_restantes.configure('Botones_restantes.TButton', background="#CECECE", foreground="black")
    estilo_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

def ingresarValores(tecla):
    if tecla >="0" and tecla <="9" or tecla =="(" or tecla ==")" or tecla ==".":
        entrada2.set(entrada2.get() + tecla)

    if tecla == "*" or tecla =="/" or tecla == "-" or tecla == "+":
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")

        entrada2.set("")

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def Ingresarvaloresteclado(event):
    tecla= event.char
    print(event)

    if tecla >="0" and tecla <="9" or tecla =="(" or tecla ==")" or tecla ==".":
        entrada2.set(entrada2.get() + tecla)

    if tecla == "*" or tecla =="/" or tecla == "-" or tecla == "+":
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")

        entrada2.set("")

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def raizCuadrada():
    entrada1.set("")
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)


def borrar(*args):

    inicio=0 
    final=len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])

def Borrar_todo(*args):
    entrada1.set("")
    entrada2.set("")


root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.Tframe', background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0,row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)


# Estilos Labels !!!!!
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel1', font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel2', font="arial 40", anchor="e")
# Entradas !!!!!!

entrada1 = StringVar()
Label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style='Label1.TLabel')
Label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style='Label2.TLabel')
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))
# Estilo para botones !!!!!!!!

estilo_botones_numeros = ttk.Style()
estilo_botones_numeros.configure('Botones_numero.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")
estilo_botones_numeros.map('Botones_numero.TButton', background=[('active', '#B9B9B9')])


estilo_botones_borrar = ttk.Style()
estilo_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilo_botones_borrar.map('Botones_borrar.TButton', forenground=[('active', '#FF000')], background=[('active', '#858585')])


estilo_botones_restantes = ttk.Style()
estilo_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilo_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])


button0 = ttk.Button(mainframe, text="0", style="Botones_numero.TButton", command=lambda: ingresarValores("0"))
button1 = ttk.Button(mainframe, text="1", style="Botones_numero.TButton", command=lambda: ingresarValores("1"))
button2 = ttk.Button(mainframe, text="2", style="Botones_numero.TButton", command=lambda: ingresarValores("2"))
button3 = ttk.Button(mainframe, text="3", style="Botones_numero.TButton", command=lambda: ingresarValores("3"))
button4 = ttk.Button(mainframe, text="4", style="Botones_numero.TButton", command=lambda: ingresarValores("4"))
button5 = ttk.Button(mainframe, text="5", style="Botones_numero.TButton", command=lambda: ingresarValores("5"))
button6 = ttk.Button(mainframe, text="6", style="Botones_numero.TButton", command=lambda: ingresarValores("6"))
button7 = ttk.Button(mainframe, text="7", style="Botones_numero.TButton", command=lambda: ingresarValores("7"))
button8 = ttk.Button(mainframe, text="8", style="Botones_numero.TButton", command=lambda: ingresarValores("8"))
button9 = ttk.Button(mainframe, text="9", style="Botones_numero.TButton", command=lambda: ingresarValores("9"))

button_clear = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar()) 
button_clearall = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton",command=lambda: Borrar_todo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: ingresarValores("("))
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: ingresarValores(")"))
button_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: ingresarValores("."))

button_division = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda: ingresarValores("/"))
button_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: ingresarValores("-"))
button_multiplicacion = ttk.Button(mainframe, text="*", style="Botones_restantes.TButton", command=lambda: ingresarValores("*"))
button_suma = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: ingresarValores("+"))

button_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: ingresarValores("="))
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda: raizCuadrada())
# Botones en pantalla ¡¡¡¡ PRIMERA FILA !!!!

button_parentesis1.grid(column=0, row=2, sticky=(W,N,E,S))
button_parentesis2.grid(column=1, row=2, sticky=(W,N,E,S))
button_clearall.grid(column=2, row=2, sticky=(W,N,E,S))
button_clear.grid(column=3, row=2, sticky=(W,N,E,S))
# SEgUNDA FILA !!!!!!!!!!

button7.grid(column=0, row=3, sticky=(W,N,E,S))
button8.grid(column=1, row=3, sticky=(W,N,E,S))
button9.grid(column=2, row=3, sticky=(W,N,E,S))
button_division.grid(column=3, row=3, sticky=(W,N,E,S))
# TERCERA FILA !!!!!

button4.grid(column=0, row=4, sticky=(W,N,E,S))
button5.grid(column=1, row=4, sticky=(W,N,E,S))
button6.grid(column=2, row=4, sticky=(W,N,E,S))
button_multiplicacion.grid(column=3, row=4, sticky=(W,N,E,S))
# CUARTA FILA !!!!!!!!!111

button1.grid(column=0, row=5, sticky=(W,N,E,S))
button2.grid(column=1, row=5, sticky=(W,N,E,S))
button3.grid(column=2, row=5, sticky=(W,N,E,S))
button_suma.grid(column=3, row=5, sticky=(W,N,E,S))
# QUINTA FILA !!!!!!!!

button0.grid(column=0, row=6, columnspan=2, sticky=(W,N,E,S))
button_punto.grid(column=2, row=6, sticky=(W,N,E,S))
button_resta.grid(column=3, row=6, sticky=(W,N,E,S))
# SEXTA FILA !!!!!!!!

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W,N,E,S))
button_raiz_cuadrada.grid(column=3, row=7, sticky=(W,N,E,S))

for child in mainframe.winfo_children():
    child.grid_configure(ipadx=10, padx=1, pady=1)

root.bind('<KeyPress-o>', temaOscuro)
root.bind('<KeyPress-c>', temaClaro)
root.bind('<Key>', Ingresarvaloresteclado)
root.bind('<KeyPress-b>', borrar)
root.bind('<KeyPress-q>', Borrar_todo)

root.mainloop()
