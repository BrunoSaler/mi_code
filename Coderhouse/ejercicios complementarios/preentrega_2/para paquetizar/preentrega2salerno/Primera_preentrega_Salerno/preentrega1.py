# -*- coding: utf-8 -*-
"""Primera pre-entrega Salerno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wKa0cQ7loi4njOebITQHoRj9koLjHV6-

Breve reseña de las funciones:

**main:** según el valor de la variable menu (la opción que elijo) llama a la función a la que quiero acceder, y luego de ejecutarse siempre vuelve a llamar al menú principal. También, como esta dentro de un while (true) y menu esta inicializada en 0, por defecto llama al menú principal al principio.

**opciones:** me muestra el menú principal y me deja ingresar la opción deseada.

**mostrar:** muestra el contenido del diccionario mayor con todos los registros. No es para nada necesario usarla como función aparte, pero lo pide la consigna. Solo se ejecuta si existe algún registro ingresado, caso contrario me dice que no hay usuarios registrados.

**es_valido:** llama a una función que verifica si la opción ingresada es un int. Luego se fija si es una opción válida (entre 1 y 5). Si no lo es me pide ingresarla devuelta y llama a la función que verifica si es número, y luego realiza el chequeo de si es válida. Esto se repite hasta que ingrese una opción válida.

**es_número:** verifica si la opción ingresada es un entero, y mientras no lo sea me pide una opción correcta.

**registro:** me permite ingresar un par usuario-contraseña para guardarlo. Si la base está vacía, lo hace sin más. Caso contrario chequea en el resto del diccionario mayor que no haya ningún registro con ese nombre de usuario, y si lo hay me avisa y no me deja ingresarlo. Solo se permite un nombre de usuario que no esté repetido, por lo que en cuanto encuentra el primero, deja de buscar (esto es útil si tengo una base grande de registros). Para poder comparar el nombre de usuario correctamente, independientemente de como lo ingrese el usuario, lo transforma a mayúsculas.

**login:** simula un inicio de sesión. Se fija si existe el nombre de usuario que ingresé, caso contrario me dice que no lo encuentra. Si y solo si lo encontró, me pide contraseña hasta 3 veces. Si la ingreso correctaamente me da como exitoso el login, sino me dice que ingresé la contraseña mal 3 veces. En el caso de haber encontrado el nombre de usuario, independientemente si me logro loguear o no, deja de buscar en el resto de los nombres de usuario del diccionario mayor, porque ya se que existe y por diseño del programa es único (esto es útil si tengo una base grande de registros). Solo se ejecuta si existe algún registro ingresado, caso contrario me dice que no hay usuarios registrados.

**guardar:** me guarda todos los pares usuario-contraseña ingresados en un archivo .txt en la raíz del gdrive del que lo ejecuta (siempre que tenga los permisos con el primer bloque de código). Los guarda numerados por orden de ingreso, y uno por renglón del .txt. Solo se ejecuta si existe algún registro ingresado, caso contrario me dice que no hay usuarios registrados.
"""

from google.colab import drive
drive.mount('/drive')

from pprint import pprint

menu=0                                                                            #donde se guarda la opción ingresada del menu. Al ponerla acá no me hace falta pasarla como argumento por varias funciones.
usuarios={}                                                                       #diccionario que va a tener diccionarios adentro, con los registros. Como es un tipo compuesto, no hace falta decirle a la funcion que es global porque siempre se pasa por referencia.

def es_valido():                                                                  #me dice si la opción ingresada es válida.
    global menu
    es_numero()
    while(menu<1 or menu>5):
        menu = input("Ingrese una opción válida: ")
        es_numero()

def es_numero():                                                                  #verifica si la opción ingresada es un número entero.
    global menu
    while (not menu.isnumeric()):
            menu = input("Ingrese una opción válida: ")
    menu=int(menu)

def opciones():                                                                   #el menú principal.
    global menu
    print("-"*90)
    print("Menu de opciones: ")
    print("-"*90)
    print("1: Registrar usuario.")
    print("2: Mostrar usuarios registrados.")
    print("3: Simular Login.")
    print("4: Guardar usuarios en un archivo de texto.")
    print("5: Finalizar programa.")
    print("-"*90)
    print("\n")
    menu=input("Ingrese un número correspondiente a una función: ")
    es_valido()

def registro():                                                                  #Ingreso de usuario-contraseña a mi diccionario mayor
    dict={}
    z=0
    if (len(usuarios)==0):                                                       #mi diccionario mayor está vacío
        dict["usuario"]=input("Ingrese un nombre de usuario: ")
        dict["usuario"]=dict["usuario"].upper()                                  #Ponga lo que ponga me lo pasa a mayúsculas, para luego comparar, sino pepe!=PEPE y no busco eso.
        dict["contraseña"]=input("Ingrese una contraseña: ")
        usuarios[len(usuarios)]=dict.copy()                                      #luego del copy, len(usuarios) pasa a ser 1
    else:                                                                        #diccionario mayor no vacío
        dict["usuario"]=input("Ingrese un nombre de usuario: ")
        dict["usuario"]=dict["usuario"].upper()
        for y in usuarios:
            existe=dict["usuario"] in usuarios[y]["usuario"]
            if (existe==True):
                print("Usuario existente.")
                z=1
                break                                                            #apenas encuentra el nombre existente sale y no sigue buscando, optimizo tiempo y recursos en el caso de que el diccionario mayor sea muy grande.
        if (z==0):
            dict["contraseña"]=input("Ingrese una contraseña: ")
            usuarios[len(usuarios)]=dict.copy()                                  #Al manejarme con len(usuarios), me aseguro que las claves del diccionario mayor siempre sean correlativas y que arranca de 0
            print("Usuario registrado.")

def mostrar():
  pprint(usuarios)
  return("Fin de base.")

def login():                                                                     #simula un login
    x=0
    z=0                                                                          #contador de veces que ingresé la contraseña
    not_found=0
    user=input("Ingrese su usuario: ")
    user=user.upper()
    for y in usuarios:
          existe=user in usuarios[y]["usuario"]
          while (existe==True):
              not_found=1                                                        #el usuario existe
              existe=False                                                       #lo vuelvo a pasar a false para que no se quede en el bucle, ya se que el usuario aparece 1 vez sola por condición de diseño del programa
              password=input("Ingrese contraseña: ")
              z=z+1
              while ((not password in usuarios[y]["contraseña"]) and z!=3):      #me permite ingresar una contraseña hasta 3 veces
                  password=input("Ingrese contraseña correcta: ")
                  z=z+1
              if (z<=3 and password in usuarios[y]["contraseña"]):
                  print("Login exitoso.")
                  x=1                                                            #ya me loguee, por lo que no quiero seguir buscando coincidencias de usuario, por diseño es único
              else:
                  print("Contraseña ingresada 3 veces erróneamente.")
                  x=1                                                            #no me loguee, pero el usuario sé que existe, por lo que no quiero seguir buscando coincidencias de usuario, por diseño es único
          if(x==1):
              break                                                              #apenas encuentra el nombre existente sale y no sigue buscando, optimizo tiempo y recursos en el caso de que el diccionario mayor sea muy grande.
    if (not_found==0):
          print("No se encuentra usuario.")

def guardar():                                                                    #función que me guarda el diccionario con diccionarios en un txt.
    mi_archivo = open("/drive/MyDrive/registros.txt",  "w")                       #escibe el archivo en la raíz del gdrive del que lo ejecuta (si le dí los permisos con el primer bloque de código).
    for y in usuarios:
        mi_archivo.write(f"{y}: ")
        mi_archivo.write(str(usuarios[y]))
        mi_archivo.write("\n")
    mi_archivo.close()
    print("Archivo guardado.")

                                                                                  #main, me redirige a la función correcta según la opción que elija.
print("Bienvenido.")
while True:
    if (menu==0):                                                                 #como inicialicé la variable en 0, la primera vez siempre pasa por acá.
        print("\n")
        opciones()
    if (menu==1):
        registro()
        menu=0                                                                    #al final de cada función, vuelvo a poner siempre la variable en 0 para que el bucle me repita las opciones y pueda volver a elegir.
    elif (menu==2):
        if (len(usuarios)==0):
            print("Sin usuarios registrados.")
        else:
            print(mostrar())
        menu=0
    elif (menu==3):
        if (len(usuarios)==0):
            print("Sin usuarios registrados.")
        else:
            login()
        menu=0
    elif (menu==4):
        if (len(usuarios)==0):
            print("Sin usuarios registrados.")
        else:
            guardar()
        menu=0
    elif (menu==5):
        print("Fin del programa, gracias por utilizar.")
        break