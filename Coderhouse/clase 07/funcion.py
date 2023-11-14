variable=15
string="No ejecuté y."

def x(i):
    resto_de_divir_con_dos = i % 2
    if resto_de_divir_con_dos == 0:
        print(f"{i} es un numero par")
    else:
        print(f"{i} es un numero impar")
    return "Fin del cálculo"

def y():
    global string #le especifico que no quiero crear la variable local string, sino que use la global, siempre al principio
    resto_de_divir_con_dos = variable % 2
    if resto_de_divir_con_dos == 0:
        print(f"{variable} es un numero par")
    else:
        print(f"{variable} es un numero impar")
    string="Ya ejecuté y."

for i in range(10):
    string_2=x(i)
    print(f"{string_2}",i+1)

#si la variable es global no hace falta pasárla como argumento porque la ve
print(string)
y()
print(string)