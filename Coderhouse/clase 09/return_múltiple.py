def func():
    return 1, 2, "beta"


def func_exotica():
    return (1, 2), "beta", (2, 3)


mi_variable = func() #devuelve una tupla

x, y, z = func() #devuelve los 3 valores separados
# xx, yy = func() se rompe

print(mi_variable)

print(x)
print(y)
print(z)


xx = func_exotica()#devuelve una tupla con tuplas

print(xx)