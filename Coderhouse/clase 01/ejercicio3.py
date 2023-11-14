cadena="acitametaM ,5.8 ,otipeP ordeP"
cadena_volteada=cadena[::-1]
print(cadena)
print(cadena_volteada)
nombre_alumno=cadena_volteada[0:12:1]#el 1 acá es redundante
nota=float(cadena_volteada[14:17:1])#el 1 acá es redundante
materia=cadena_volteada[19:29:1]#el 29 como es llevar al final aca es redundante, el 1 acá es redundante
print(nombre_alumno)
print(nota)
print(materia)