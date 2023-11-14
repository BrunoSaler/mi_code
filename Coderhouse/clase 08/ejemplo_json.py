import json

mi_departamento = {
  "departamento": 8,
  "activo": True,
  "deudas": None,
  "nombre": "Ventas",
  "director": "Juan Rodríguez",
  "empleados":[
    {
      "nombre":"Pedro",
      "apellido":"Fernández"
    },{
      "nombre":"Jacinto",
      "apellido":"Benavente"
    }
  ]
}

mi_archivo = open("departamento.json", "w")

json.dump(mi_departamento, mi_archivo)

mi_archivo.close()


# Leer el archivo de dos maneras distintas

mi_archivo_de_lectura_1 = open("departamento.json", "r")
contenido_1 = mi_archivo_de_lectura_1.read()#lo lee como string

mi_archivo_de_lectura_2 = open("departamento.json", "r")
contenido_2 = json.load(mi_archivo_de_lectura_2)#lo lee como json, puede ser tipo lista o diccionario
#aca es un diccionario con diccionarios adentro

#print(type(contenido_1))
#print(contenido_1["director"]) como es un stringno lo puedo acceder como un diccionario, se rompe el programa

print(type(contenido_2))
print(contenido_2["director"])
print(contenido_2["empleados"])#veo con las siguientes 3 líneas como voy accediendo a los distintos campos del dicc
print(contenido_2["empleados"][0])
print(contenido_2["empleados"][0]["nombre"])