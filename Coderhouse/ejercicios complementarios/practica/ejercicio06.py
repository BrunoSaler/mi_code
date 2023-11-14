a=int(input("Dígame cuantos números va a ingresar: "))
b=float(0)
for i in range(a):
    print(f"Ingrese el número {i+1}: ")
    b=b+float(input())
print(f"El promedio es {b/a}.")