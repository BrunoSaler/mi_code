lista_1=[]
lista_2=[]
lista_1.append(int(456789))
lista_1.append("Hola Mundo")#append es siempre de a uno
lista_2.extend(["Hola y adios",int(5555),float(3.1416)])#extend es como un append de varios elementos
lista_3=lista_1[0:1:1]
lista_4=lista_2[1:-1:1]
lista_5=lista_4+lista_3
lista_6=lista_3+lista_4
print(lista_1)
print(lista_2)
print(lista_3)
print(lista_4)
print(lista_5)
print(lista_6)
print("-"*20)
lista_7=[1,2,3,4,5]
variable=lista_7.pop()#pop en realidad no borra, asigna el último momento adonde se lo indique, si no indico nada se borra
print(lista_7)
print(variable)