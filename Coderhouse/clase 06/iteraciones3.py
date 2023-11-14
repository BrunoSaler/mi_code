dict_1 = {
    "clave_alpha": "one",
    "clave_beta": "two",
    "clave_delta": "three"
}


for xx in dict_1.items():
    print(xx)


print("-" * 90)
for xx in dict_1.items(): #aca la variable que crea el for es una tupla
    print(xx[0])
    print(xx[1])
    print("-" * 20)

print("-" * 90)
for clave, valor in dict_1.items(): #aca es lo mismo pero el for en vez de crear una tupla crea 2 variables
    print(clave)
    print(valor)
    print("-" * 20)