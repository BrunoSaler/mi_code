x = input("Ingrese un año: ")

def bisiesto():
    global x              
    while (not x.isnumeric()):#solo funciona con int
            x = input("Ingrese un año correcto: ")
    x=int(x)
    if((x%4==0 and x%100!=0) or x%400==0):
            print(f"El año {x} es bisiesto.")
    else:
            print(f"El año {x} no es bisiesto.")

bisiesto()