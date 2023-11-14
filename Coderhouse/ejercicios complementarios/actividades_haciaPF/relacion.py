a=input("Ingrese un número: ")
b=input("Ingrese otro número: ")

def relacion():
    if (a>b):
        return(1)
    elif (a<b):
        return(-1)
    elif(a==b):
        return 0

while (True):#en este bucle infinito intento hacer algo, si puede sale del while con el break, si da error me sigue pidiendo el dato
    try:
        a = float(a)
        break
    except ValueError:
        a = input("Ingrese el primer número correctamente: ")
while (True):
    try:
        b = float(b)
        break
    except ValueError:
        b = input("Ingrese el segundo número correctamente: ")
print(relacion())