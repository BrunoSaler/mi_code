mi_lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print("**********************************************************************")
print(mi_lista)
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[1])
print("**********************************************************************")
print(mi_lista[-1])
print(mi_lista[-2])
print("**********************************************************************")
print(mi_lista[0:2])
print(mi_lista[0:3])
print("**********************************************************************")
print(mi_lista[0:7:2])
print(mi_lista[0:7:3])
print("**********************************************************************")
print(mi_lista[-2:])
print(mi_lista[-4:])
print("**********************************************************************")
print(mi_lista)
mi_lista[2]="Pochito"
print(mi_lista)
print("**********************************************************************")
mi_lista[0:2]=["El","gato"]
print(mi_lista)
print("**********************************************************************")
mi_lista[0:3]=[]
print(mi_lista)
print("**********************************************************************")
mi_lista[0:]=[]
print(mi_lista)#vacié la lista
print("**********************************************************************")
mi_lista_b=["a","b"]
print(mi_lista_b)
mi_lista_b.append("agregado")#agrega siempre al final
print(mi_lista_b)
print("**********************************************************************")
mi_lista_b.pop(1)#borro uno en el medio
print(mi_lista_b)
print("**********************************************************************")
mi_lista_b.pop()#borro el último
print(mi_lista_b)
print("**********************************************************************")
mi_lista = ["a", "b", "c", "d", "e", "f", "c", "h", "i"]
print(mi_lista.count("c"))#cuantas veces esta c en la lista
print(mi_lista.index("c"))#el índice de c en la lista, siempre tira solo el primero
print("**********************************************************************")
mi_lista_b=[1,2,3]
print(mi_lista+mi_lista_b)
print(mi_lista_b+mi_lista)