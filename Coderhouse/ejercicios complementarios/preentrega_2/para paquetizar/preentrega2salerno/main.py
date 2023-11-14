from pprint import pprint
from .clases import *

def main():
    print("Bienvenido.")
    registros = base_de_datos("BASE MADRE")
    try:                                                                #si puede, levanta un archivo preexistente, no hay drama con el nombre porque se lo impongo yo
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
            if(registros[email]==False):
                print(registros.ingresar_usuario(email))
            else:
                print("El correo ingresado ya se encuentra registrado.")
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
                print(registros.guardar_archivo())
            menu=0
        elif (menu==7):
            print("Fin del programa, gracias por utilizar.")
            break