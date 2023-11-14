a=int(input("ingrese un número impar: "))
b=0
c=a%2

while (b==0):
    if (c==0):
        a=int(input("ingrese un número impar: "))
        c=a%2
    else:
        print("Tu número es impar")
        b=1

print("Fin del programa")

    