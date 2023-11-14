import math

radio=input("Ingrese el radio del circulo en cm.: ") #las inicializo para que no me de error
area=float(0)

def area_circulo():
    global area
    area=(radio**2)*math.pi

while (True):#en este bucle infinito intento hacer algo, si puede sale del while con el break, si da error me sigue pidiendo el dato
    try:
        radio = float(radio)
        break
    except ValueError:
        radio = input("Ingrese el radio del circulo en cm. correctamente: ")
area_circulo()
print(f"El área del círculo es {area} cm^2.")