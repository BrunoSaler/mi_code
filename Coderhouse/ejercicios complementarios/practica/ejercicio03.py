a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
d=0 #lo uso como flag
print("Opciones disponibles:")
print("1: suma los 2 números.")
print("2: resta los 2 números.")
print("3: multiplica los 2 números.")
print("4: Fin del programa.")
c=int(input("Ingrese la opción deseada: "))
while (d==0):
    if (c==1):
        print(a+b)
        d=1
        break
    elif (c==2):
        print(a-b)
        d=1
        break
    elif (c==3):
        print(a*b)
        d=1
        break
    elif (c==4):
        d=1
        break
    elif (c!=1 and c!=2 and c!=3 and c!=4):
        c=int(input("Ingrese una opción válida: "))
if (d==1):
    print("Programa terminado.")