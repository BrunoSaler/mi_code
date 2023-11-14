print("Bienvenido")
nombre=input("Ingrese su nombre: ")
apodo=input("Ingrese su apodo: ")
edad=int(input("Ingrese su edad: "))#en edad va a guardar un int en vez de un string, input por defecto siempre toma un string
print(f"{nombre} tiene {edad} años.")#entre argumentos, print agrega siempre un espacio
print(f"Le dicen \"{apodo}\"")
cuenta=((4 + 8) / 2 * 5) ** 2 - (9 + 3) / 2
print(f"{nombre} la cuenta da esto\n{cuenta}")