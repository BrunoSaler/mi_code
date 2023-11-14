mi_archivo = open(r"C:\Users\Bruno\source\repos\Coderhouse\clase 08\mi_primer_archivo.txt", "w")#con la r de raw le digo que no me tome la \ como para hacer una acción (ejemplo retorno de carro) la uso siempre que quiero poner un directorio en windows porque linux o mac usa la barra para elotro lado
mi_archivo.write("Esta es la primer linea que escribo!")
mi_archivo.write("Esta es la segunda linea que escribo!")
mi_archivo.writelines(
    [
        "Esta es la primer linea que escribo!\n",
        "Esta es la segunda linea que escribo!\n",
        "=)"
    ]
)
mi_archivo.close()

ruta=r"C:\Users\Bruno\source\repos\Coderhouse\clase 08"
mi_archivo = open(ruta + r"\mi_segundo_archivo.txt", "w")
mi_archivo.write("línea auxiliar")
mi_archivo.close()