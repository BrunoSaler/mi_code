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