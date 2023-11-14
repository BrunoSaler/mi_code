year=input("Ingrese su año de nacimiento: ") #siempre toma un string
#si lo casteo acá y le ingreso un texto, se rompe el programa

if not year.isnumeric():
    print("Ingrese un valor entero.")
else:
    year=int(year)

if(year>=1920 and year<=1945):
    print("Su generación es ""Generación silenciosa"".")
elif(year>=1946 and year<=1964):
    print("Su generación es ""Baby Boomer"".")
elif(year>=1965 and year<=1979):
    print("Su generación es ""Generación X"".")
elif(year>=1980 and year<=2000):
    print("Su generación es ""Generación Y"".")
elif(year>=2001 and year<=2010):
    print("Su generación es ""Generación Z"".")
elif(year<1920 or year>2010):
    print("No sé cuál es su generación.")