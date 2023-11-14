#sin usar el método de variable global
x = input("Ingrese un año: ")

def bisiesto(x):             
    while (True):#en este bucle infinito intento hacer algo, si puede sale del while con el break, si da error me sigue pidiendo el año
        try:
            x = int(x)
            break
        except ValueError:
            x = input("Ingrese un año correcto: ")
    if((x%4==0 and x%100!=0) or x%400==0):
            print(f"El año {x} es bisiesto.")
    else:
            print(f"El año {x} no es bisiesto.")

bisiesto(x)