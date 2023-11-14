from pprint import pprint
from datetime import datetime
import json

#clases
class usuario:
    def __init__(self, email, password, nombre, nacimiento):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.compras = {}

    def mostrar_datos(self):                                                            #metodo 1
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Fecha de nacimiento: {self.nacimiento}")

    def edad(self, nacimiento2):                                                        #metodo 2
        edad=datetime.now()-nacimiento2       #la resta da como resultado en days
        edad=edad/365
        return edad.days                      #devuelvo solo los dias,sin minutos ni segundos
    
    def __str__(self):                                                                  #metodo 3
        return self.nombre

class base_de_datos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro_de_usuarios = {}

    def cargar_archivo(self):                                                           #metodo 1
        mi_archivo = open("datos_negocio.json", "r")
        self.registro_de_usuarios = json.load(mi_archivo)
        mi_archivo.close()

    def guardar_usuario(self, usuario):                                                 #metodo 2
        self.registro_de_usuarios[usuario.email] = {
            "nombre": usuario.nombre,
            "password": usuario.password,
            "nacimiento": usuario.nacimiento,
            "compras": usuario.compras
        }

    def ver_usuario(self, email):                                                       #metodo 3
        return self.registro_de_usuarios[email]
    
    def ingresar_compra(self, email):                                                   #metodo 4
        stringaux="si"
        y=len(self.registro_de_usuarios[email]["compras"])+1
        dict={}
        while (stringaux=="si"):
            fecha_de_compra=input("Ingrese la fecha de compra en formato d-m-aaaa: ")
            x=0
            while (x==0):
                try:
                    fecha_de_compra=datetime.strptime(fecha_de_compra, "%d-%m-%Y")
                    x=1
                except:
                    fecha_de_compra=input("ingrese la fecha de compra correctamente en formato d-m-aaaa: ")
            fecha_de_compra=date_format(fecha_de_compra)
            sucursal=input("Ingrese la sucursal donde se realizó la compra: ")
            sucursal=sucursal.upper()
            producto=input("Ingrese el producto adquirido: ")
            producto=producto.upper()
            cantidad=input("Ingrese la cantidad de producto adquirida: ")
            cantidad=es_numero(cantidad)
            dict[f"compra {y}"]={
                                "Fecha de compra": fecha_de_compra,
                                "sucursal": sucursal,
                                "producto": producto,
                                "cantidad": cantidad
                                }
            self.registro_de_usuarios[email]["compras"].update(dict)
            print("Compra ingresada.")
            stringaux=input("¿Desea agregar otra compra? (si/no): ")
            stringaux=stringaux.lower()
            if (stringaux=="si" or stringaux=="no"):
                pass            
            else:    
                stringaux=input("Ingrese la opción correcta, ¿Desea agregar otra compra? (si/no): ")
                stringaux=stringaux.lower()     
            y=y+1
        return "Gracias por ingresar la compra, se agregará a la base de datos."

    def mostrar_registro(self):                                                         #metodo 5
        return self.registro_de_usuarios
    
    def guardar_archivo(self):                                                          #metodo 6
        mi_archivo = open("datos_negocio.json", "w")
        json.dump(self.registro_de_usuarios, mi_archivo)
        mi_archivo.close()
    
    def login(self, email):
        x=0 
        password=input("Ingrese contraseña: ")
        x=x+1
        while (self.registro_de_usuarios[email]["password"]!=password and x!=3):
            password=input("Ingrese contraseña correcta: ")
            x=x+1
        if (x<=3 and self.registro_de_usuarios[email]["password"]==password):
            return "Login exitoso."                                                          
        else:
            return "Contraseña ingresada 3 veces erróneamente."
    
    def __str__(self):                                              
        return self.nombre
    
    def __len__(self):                                             
        return len(self.registro_de_usuarios)
    
    def __getitem__(self, email):                                   
        return self.registro_de_usuarios.get(email, False)

#funciones

def opciones(menu):                                                 #el menú principal.                      
    print("-"*90)
    print("Menu de opciones: ")
    print("-"*90)
    print("1: Registrar usuario.")
    print("2: Mostrar todos los usuarios registrados.")
    print("3: Mostrar un usuario particular.")
    print("4: Simular Login.")
    print("5: Ingresar compra.")
    print("6: Guardar usuarios en un archivo.")
    print("7: Finalizar programa.")
    print("-"*90)
    print("\n")
    menu = input("Ingrese un número correspondiente a una función: ")
    menu = es_valido(menu)
    return menu

def es_valido(menu):                                                #me dice si la opción ingresada es válida.                  
    menu = es_numero(menu)
    while(menu<1 or menu>7):
        menu = input("Ingrese una opción válida: ")
        menu = es_numero(menu)
    return menu

def es_numero(menu):                                                #verifica si la opción ingresada es un número entero.                       
    while (not menu.isnumeric()):
        menu = input("Ingrese un número válido: ")
    menu = int(menu)
    return menu

def date_format(date):                                              #le da formato a las fechas
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]                                  #como la tupla arranca del elemento 0, le debo de restar 1
    year = date.year
    return f"{day} de {month} de {year}"

def ingresar_usuario(email):                                        #ingresa un usuario a la base
    if (registros[email]==False):
        nombre=input("Ingrese su nombre completo: ")
        nombre=nombre.upper()
        password=input("Ingrese una contraseña: ")
        x=0
        nacimiento=input("Ingrese su fecha de nacimiento en formato d-m-aaaa: ")
        while (x==0):
            try:
                nacimiento=datetime.strptime(nacimiento, "%d-%m-%Y")
                nacimiento2=nacimiento
                x=1
            except:
                nacimiento=input("Ingrese la fecha de nacimiento correctamente en formato d-m-aaaa: ")
        newuser=usuario(email, password, nombre, date_format(nacimiento))
        print("La información ingresada fue:")
        print("-"*45)
        newuser.mostrar_datos()
        print(f"El usuario ingresado tiene {newuser.edad(nacimiento2)} años.")
        print("-"*45)
        registros.guardar_usuario(newuser)
        return f"El usuario {newuser} fue registrado en la base de datos {registros}"
    else:
        return "El correo ingresado ya se encuentra registrado"

#main
print("Bienvenido.")
registros = base_de_datos("BASE MADRE")
try:                                                                #si puede, levanta un archivo preexistente, no hay dramacon el nombre porque se lo impongo yo
    registros.cargar_archivo()
    print("Base de datos recuperada correctamente.")
except Exception:
    print("Archivo no existente. No pueden cargarse datos preexistentes.")
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
                print(registros.login(email))
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
                print(registros.ingresar_compra(email))
        menu=0
    elif (menu==6):
        if (len(registros)==0):
            print("Sin usuarios registrados.")
        else:
            registros.guardar_archivo()
        menu=0
    elif (menu==7):
        print("Fin del programa, gracias por utilizar.")
        break