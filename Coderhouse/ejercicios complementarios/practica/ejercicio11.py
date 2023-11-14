lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

print(lista)

lista2=lista.copy()
for i in lista2:
    while (lista2.count(i)>1):
        lista2.remove(i)#con todo el for remuevo los duplicados, dejando solo uno de cada uno
print(lista2)

lista2.sort(reverse=True)
print(lista2)

for i in lista2: #i es cada uno de los elementos de lista2, no el índice
    if i%2==1:
        lista2.remove(i)
print(lista2)

lista2.insert(0,sum(lista2))
print(lista2)
print(lista)