from datetime import datetime
from funciones import *
import json

class usuario:                                                                          
    def __init__(self, email, password, nombre, nacimiento):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.nacimiento = nacimiento                                                    #es la fecha con el formato de da_format, ya es un string
        self.compras = {}

    def mostrar_datos(self):                                                            #me muestra el usuario que ingrese
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Fecha de nacimiento: {self.nacimiento}")

    def edad(self, nacimiento2):  
        hoy=datetime.today()                                                      #me calcula cuantos años tiene el usuario
        edad=hoy.year-nacimiento2.year-((hoy.month,hoy.day)<(nacimiento2.month,nacimiento2.day))      #esta resta da como resultado en days, nacimiento2 es la fecha de cacimiento sin aplicar date_format
        return edad
    
    def __str__(self):                                                                  #devuelve el nombre del usuario
        return self.nombre

class base_de_datos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro_de_usuarios = {}

    def cargar_archivo(self):                                                           #carga un archivo para recuperar una base existente, si puede
        mi_archivo = open("datos_negocio.json", "r")
        self.registro_de_usuarios = json.load(mi_archivo)
        mi_archivo.close()

    def ver_usuario(self, email):                                                       #me muestra un usuario en particular
        return self.registro_de_usuarios[email]
    
    def ingresar_compra(self, email):                                                   #ingresa compras, si recupera un archivo se van agregando a la base recuperada
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

    def mostrar_registro(self):                                                         #me devuelve la base completa
        return self.registro_de_usuarios
    
    def guardar_archivo(self):                                                          #guarda un json
        mi_archivo = open("datos_negocio.json", "w")
        json.dump(self.registro_de_usuarios, mi_archivo)
        mi_archivo.close()
        return f"{self} respaldada correctamente."
    
    def login(self, email):                                                             #simula un login, me deja ingresar hasta 3 veces la contraseña
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
    
    def ingresar_usuario(self, email):                                                 #ingresa un usuario a la base
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
        self.registro_de_usuarios[newuser.email] = {
                "nombre": newuser.nombre,
                "password": newuser.password,
                "nacimiento": newuser.nacimiento,
                "compras": newuser.compras
                }
        return f"El usuario {newuser} fue registrado en la base de datos {self}"

    def __str__(self):                                              
        return self.nombre
    
    def __len__(self):                                             
        return len(self.registro_de_usuarios)
    
    def __getitem__(self, email):                                   
        return self.registro_de_usuarios.get(email, False)