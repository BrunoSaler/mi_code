from time import sleep, time
import random

nombre_de_archivo =  f"mi_archivo_{time()}.txt" #le agrega time al nombre
mi_archivo = open(r"C:\Users\Bruno\source\repos\Coderhouse\clase 08\\" + nombre_de_archivo,  "w")
#cuando quiero especificar una ruta y luego agregarle dinámicamente el nombre, con \\ al finalfunciona bien
#si dejo \ y un espacio, me crea el archivo pero con un espacio al principio
#si no pongo ninguna barra, me creaun archivo en eldirectorio superior a clase 08 que se llama clase 08 + nombre
for i in range(10):
    xx = str(random.randint(0, 19))
    mi_archivo.write(xx)
    # mi_archivo.write(",")
    mi_archivo.write("\n")

mi_archivo.close()