from pprint import pprint

usuarios={}                                                                       #diccionario que va a tener diccionarios adentro, con los registros. Como es un tipo compuesto, no hace falta decirle a la funcion que es global porque siempre se pasa por referencia.

def es_valido(menu):                                                                  #me dice si la opción ingresada es válida.
    menu = es_numero(menu)
    while(menu<1 or menu>5):
        menu = input("Ingrese una opción válida: ")
        menu = es_numero(menu)
    return menu

def es_numero(menu):                                                                  #verifica si la opción ingresada es un número entero.
    while (not menu.isnumeric()):
        menu = input("Ingrese una opción válida: ")
    menu = int(menu)
    return menu

def opciones(menu):                                                                   #el menú principal.
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
    menu = input("Ingrese un número correspondiente a una función: ")
    menu = es_valido(menu)
    return menu

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
    mi_archivo = open("registros.txt",  "w")                                        
    for y in usuarios:
        mi_archivo.write(f"{y}: ")
        mi_archivo.write(str(usuarios[y]))
        mi_archivo.write("\n")
    mi_archivo.close()
    print("Archivo guardado.")

                                                                                  #main, me redirige a la función correcta según la opción que elija.
print("Bienvenido.")
menu=0
while True:
    if (menu==0):                                                                 #como inicialicé la variable en 0, la primera vez siempre pasa por acá.
        print("\n")
        menu = opciones(menu)
    elif (menu==1):
        registro()
        menu=0                                                                    #al final de cada función, vuelvo a poner siempre la variable en 0 para que el bucle me repita las opciones y pueda volver a elegir.
    elif (menu==2):
        if (len(usuarios)==0):
            print("Sin usuarios registrados.")
        else:
            pprint(usuarios)
            print("Fin de base.")
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