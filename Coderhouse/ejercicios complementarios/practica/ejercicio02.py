matriz=[[1,5,1],[2,1,2],[3,0,1],[1,4,4]]
print(matriz)

for i in range(4):
    auxiliar=[sum(matriz[i])]
    matriz[i]=matriz[i]+auxiliar
print(matriz)