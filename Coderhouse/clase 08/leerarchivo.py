mi_archivo = open("mi_archivo_1697588193.7525046.txt", "r")#reemplazar con elnombre de archivo
#si lo pongo sin ruta me tengo que asegurar con terminal de que este parado en el directorio


#contenido = mi_archivo.read()
#print(contenido)

contenido2 = mi_archivo.read()
print(contenido2)#no lo imprime porque la posición quedó al final,no se resetea
mi_archivo.seek(0)#vuelvo el cursor al inicio

mi_archivo.seek(1)#el salto de línea lo cuenta como 2 posiciones, 1 es la primera
contenido = mi_archivo.read()
print(contenido)

mi_archivo.seek(2)#la segunda del salto de línea
contenido = mi_archivo.read()
print(contenido)

mi_archivo.seek(3)#aca ya no arranca imprimiendo el espacio
contenido = mi_archivo.read()
print(contenido)

mi_archivo.close()