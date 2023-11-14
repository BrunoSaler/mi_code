dict={}

dict["nombre"]=input("Ingrese su nombre: ")
dict["edad"]=int(input("Ingrese su edad: "))
dict["dirección"]=input("Ingrese su dirección: ")
print(f"Su nombre es {dict['nombre']}, su edad es {dict['edad']} y su dirección es {dict['dirección']}") 
#cuando uso f-print, no puedo poner corchete adentro de corchete, tengo que usar alt+39
print(dict)