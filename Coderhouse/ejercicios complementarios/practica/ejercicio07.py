lista=[0,1,3,5,8]
a=0
b=float(input("Ingrese un valor del 0 al 9: "))

while (a==0):
    if (b<0 or b>89):
        b=float(input("Ingrese un valor del 0 al 9: "))
    else:
        a=1

if(b in lista):
    print("Su valor se encuentra en la lista")
else:
    print("Su valor no se encuentra en la lista")