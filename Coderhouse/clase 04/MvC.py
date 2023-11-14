nombre=input("Ingrese su nombre: ")
preferencia=input("¿Cuál es tu preferencia (M o C)?: ")
inicial=nombre[0:1:1]
grupoA=0

if (inicial.upper()<="M" and preferencia.upper()=="M"):
    print("Sos del grupo A.")
    grupoA=1
elif (inicial.upper()>"M" and preferencia.upper()=="C"):
    print("Sos del grupo A.")
    grupoA=1
elif (grupoA==0):
    print("Sos del grupo B.")