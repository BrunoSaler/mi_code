x=int(input("Ingrese cuántos números va a ingresar: "))
lista = []
lista_par=[]
lista_impar=[]

def separar():
    global lista_par, lista_impar
    for i in range(x):
        if(lista[i]%2==0):
            lista_par.append(lista[i])
        else:
            lista_impar.append(lista[i])

for i in range(x):
    lista.append(int(input("Ingrese un número: ")))
separar()
print(f"{lista_par}\n{lista_impar}")