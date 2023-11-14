dict={1:"a" , 2:"dos", 3:"tres"}

x=dict[1]
print(x)

#x=dict(4) Esto da error,porque 4 no existe

x=dict.get(4, "no lo encuentro")
print(x)