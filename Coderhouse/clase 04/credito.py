edad=input("Ingrese la edad del candidato: ")
while (not edad.isnumeric()):
    edad=input("Ingrese una edad válida: ")
edad=int(edad)

antiguedad=input("Ingrese la antiguedad del candidato: ")
while (not antiguedad.isnumeric()):
    antiguedad=input("Ingrese una antiguedad válida: ")
antiguedad=int(antiguedad)

ingreso=input("Ingrese el salario neto del candidato: ")
while (not ingreso.isnumeric()):
    ingreso=input("Ingrese un salario válido: ")
ingreso=int(ingreso)

aprobado=0

if (edad>=18 and ingreso>=4000):
    print("Su crédito está aprobado.")
    aprobado=1
elif (edad>=18 and antiguedad>=3 and ingreso>2500):
    print("Su crédito está aprobado.")
    aprobado=1
elif (aprobado==0):
    print("Crédito rechazado.")