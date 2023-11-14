from datetime import datetime

def date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1] #como la tupla arranca del elemento 0, le debo de restar 1
    year = date.year
    return f"{day} de {month} de {year}"

x=0
nacimiento=input("ingrese la fecha de nacimiento en formato d-m-aaaa: ")
while (x==0):
    try:
        nacimiento=datetime.strptime(nacimiento, "%d-%m-%Y")
        x=1
    except:
        nacimiento=input("ingrese la fecha de nacimiento correctamente en formato d-m-aaaa: ")

print(date_format(nacimiento))
edad=datetime.now()-nacimiento #la resta da como resultado en days
edad=edad/365
print(f"{edad.days} años") #queda en days por la cuenta, pero son los años
