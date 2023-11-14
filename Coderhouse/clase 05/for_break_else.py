from time import sleep


for numero in range(10):
    sleep(1)
    print(numero)
    if numero == 2:
        print(".... 1")
        continue
    elif numero == 8:
        print(".... 2")
        break #si lo ejecuta termina el bucle y no ejecuta el else
        pass #aca no hace nada
else:
    print("..... 3")
    print("Se terminó de iterar y numero vale: ", numero)