xx = 0
while xx < 10:
    xx += 1
    if xx == 7:
        pass
    print(xx)
else:
    print("fin de ciclo")
print("---------------------------------")
n = 0
while n < 10:
    n += 1
    if n == 2:
        pass #sigue ejecutando el bucle, evita que me de error por no poner nada en el else
    print('n vale' , n) 

print("---------------------------------")

n = 0
while n < 10:
    n += 1
    if n == 2:
        pass #sigue ejecutando el bucle, el print esta dentro del if
        print('n vale' , n)
print("---------------------------------")
c = -3
while c < 10:
    c += 1
    if c == 2:
        pass #evita que me de un error por no poner nada
    print('c vale', c)

