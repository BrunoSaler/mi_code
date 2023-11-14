base=input("Ingrese la longitud de la base del rectángulo en cm.: ")
altura=input("Ingrese la longitud de la altura del rectángulo en cm.: ")
area=float(0)

def area_rectangulo():
    global area
    area=base*altura

while (True):#en este bucle infinito intento hacer algo, si puede sale del while con el break, si da error me sigue pidiendo el dato
    try:
        base = float(base)
        break
    except ValueError:
        base = input("Ingrese la longitud de la base del rectángulo en cm. correctamente: ")
while (True):
    try:
        altura = float(altura)
        break
    except ValueError:
        altura = input("Ingrese la longitud de la altura del rectángulo en cm. correctamente: ")
area_rectangulo()
print(f"El área del rectángulo es {area} cm^2.")