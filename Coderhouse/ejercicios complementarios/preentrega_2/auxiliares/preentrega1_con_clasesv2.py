from pprint import pprint
from datetime import datetime


#clases
class usuario:
    def __init__(self, email, password, nombre, nacimiento):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.compras = {}

    def ingresar_reclamo(self):
        pass

    def __str__(self):
        return self.nombre

class base_de_datos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro_de_usuarios = {}

    def guardar_usuario(self, usuario):
        self.registro_de_usuarios[usuario.email] = {
            "nombre": usuario.nombre,
            "password": usuario.password,
            "nacimiento": usuario.nacimiento,
            "compras": usuario.compras
        }

    def ver_usuario(self, email):
        return self.registro_de_usuarios[email]
    
    def ingresar_compra(self, email, dict):
        self.registro_de_usuarios[email]["compras"].update(dict)

    def mostrar_registro(self):
        return self.registro_de_usuarios
    
    def __str__(self):
        return self.nombre
    
    def __len__(self):
        return len(self.registro_de_usuarios)
    
    def __getitem__(self, email):
        return self.registro_de_usuarios.get(email, False)
    







#funciones

def opciones(menu):                                                                   
    print("-"*90)
    print("Menu de opciones: ")
    print("-"*90)
    print("1: Registrar usuario.")
    print("2: Mostrar todos los usuarios registrados.")
    print("3: Mostrar un usuario particular.")
    print("4: Simular Login.")
    print("5: Ingresar compra.")
    print("6: Ingresar reclamo.")
    print("7: Guardar usuarios en un archivo.")
    print("8: Finalizar programa.")
    print("-"*90)
    print("\n")
    menu = input("Ingrese un número correspondiente a una función: ")
    menu = es_valido(menu)
    return menu

def es_valido(menu):                                                                  
    menu = es_numero(menu)
    while(menu<1 or menu>8):
        menu = input("Ingrese una opción válida: ")
        menu = es_numero(menu)
    return menu

def es_numero(menu):                                                                  
    while (not menu.isnumeric()):
        menu = input("Ingrese un número válido: ")
    menu = int(menu)
    return menu

def date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]     #como la tupla arranca del elemento 0, le debo de restar 1
    year = date.year
    return f"{day} de {month} de {year}"

def ingresar_usuario(email):
    if (registros[email]==False):
        nombre=input("Ingrese su nombre completo: ")
        nombre=nombre.upper()
        password=input("Ingrese una contraseña: ")
        x=0
        nacimiento=input("Ingrese su fecha de nacimiento en formato d-m-aaaa: ")
        while (x==0):
            try:
                nacimiento=datetime.strptime(nacimiento, "%d-%m-%Y")
                x=1
            except:
                nacimiento=input("Ingrese la fecha de nacimiento correctamente en formato d-m-aaaa: ")
        newuser=usuario(email, password, nombre, date_format(nacimiento))
        registros.guardar_usuario(newuser)
        return f"El usuario {newuser} fue registrado en la base de datos {registros}" #aca uso el método __str__
    else:
        return "El correo ingresado ya se encuentra registrado"

def login(email):                                                                   
    x=0 
    password=input("Ingrese contraseña: ")
    x=x+1
    while (registros.registro_de_usuarios[email]["password"]!=password and x!=3):
        password=input("Ingrese contraseña correcta: ")
        x=x+1
    if (x<=3 and registros.registro_de_usuarios[email]["password"]==password):
        return "Login exitoso."                                                          
    else:
        return "Contraseña ingresada 3 veces erróneamente."

def entrar_compra(email):
    stringaux="si"
    x=0
    while (stringaux=="si"):
        fecha_de_compra=input("Ingrese la fecha de compra en formato d-m-aaaa: ")
        while (x==0):
            try:
                fecha_de_compra=datetime.strptime(fecha_de_compra, "%d-%m-%Y")
                x=1
            except:
                fecha_de_compra=input("ingrese la fecha de compra correctamente en formato d-m-aaaa: ")
        x=0
        fecha_de_compra=date_format(fecha_de_compra)
        sucursal=input("Ingrese la sucursal donde se realizó la compra: ")
        sucursal=sucursal.upper()
        dict={fecha_de_compra:{sucursal:{}}}
        dict2={}
        stringaux2="si"
        y=1
        while(stringaux2=="si"):
            producto=input("Ingrese el producto adquirido: ")
            producto=producto.upper()
            cantidad=input("Ingrese la cantidad de producto adquirida: ")
            cantidad=es_numero(cantidad)
            dict2[f"producto {y}"]={"producto": producto, "cantidad": cantidad, "reclamo":"Ninguno", "rec_resuelto":"No"}
            stringaux2=input("¿Desea agregar otro producto? (si/no): ")
            stringaux2=stringaux2.lower()
            if (stringaux2=="si"):
                y=y+1
        dict[fecha_de_compra][sucursal].update(dict2)
        registros.ingresar_compra(email, dict)
        print("Compra ingresada.")
        stringaux=input("¿Desea agregar otra compra de distinta fecha? (si/no): ")
        stringaux=stringaux.lower()
    return "Gracias por ingresar la compra, se agregará a la base de datos."

#main
print("Bienvenido.")
registros = base_de_datos("BASE MADRE")
menu=0
while True:
    if (menu==0):                                                                 
        print("\n")
        menu = opciones(menu)
    elif (menu==1):
        email=input("Ingrese un email, el que será su nombre de usuario: ")
        email=email.lower()
        print(ingresar_usuario(email))
        menu=0
    elif (menu==2):
        if (len(registros)==0):
            print("Sin usuarios registrados.")
        else:
            pprint(registros.mostrar_registro())
            print("Fin de base.")
        menu=0
    elif (menu==3):
        if (len(registros)==0):
            print("Sin usuarios registrados.")
        else:
            email=input("Ingrese un email: ")
            email=email.lower()
            if (registros[email]==False):
                print("El email ingresado no se encuentra registrado.") 
            else:   
                pprint(registros[email])
        menu=0
    elif (menu==4):
        if (len(registros)==0):
            print("Sin usuarios registrados.")
        else:
            email=input("Ingrese un email: ")
            email=email.lower()
            if (registros[email]==False):
                print("El email ingresado no se encuentra registrado.")
            else:
                print(login(email))
        menu=0
    elif (menu==5):
        if (len(registros)==0):
            print("Sin usuarios registrados.")
        else:
            email=input("Ingrese un email: ")
            email=email.lower()
            if (registros[email]==False):
                print("El email ingresado no se encuentra registrado.")
            else:
                print(entrar_compra(email))
        menu=0

    elif (menu==8):
        print("Fin del programa, gracias por utilizar.")
        break














#try:
#    mi_archivo = open("datos_negocio.json", "r")
#    registros.registro_de_usuarios = json.load(mi_archivo)
#    mi_archivo.close()
#    if (len(registros.registro_de_usuarios)==0):
#        print("El archivo de datosexiste, pero esta vacío.")
#except Exception:
#    print("Archivo no existente. No se pueden cargar registros preexistentes")
