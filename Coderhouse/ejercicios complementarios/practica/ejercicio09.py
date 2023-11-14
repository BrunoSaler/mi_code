c1={"Inglaterra", "USA", "México"}
print(c1)

c2={"Islandia","Italia","Argentina","Portugal","USA"}
print(c2)

c3=c1.union(c2)
print(c3)

c3.discard("Italia")
c3.discard("Chile")#si uso remove da error

print(c3)
