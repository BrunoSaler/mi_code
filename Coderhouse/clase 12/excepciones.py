def dividir (a,b):
    try:
        return a/b
    except Exception as e: # puedo poner en vez de exception un tipo específico para que capture solo ese
        return f"Error {e}"
    
def dividir2 (a,b):
    try:
        resultado=a/b
    except ZeroDivisionError as e:
        return f"Error reconocido {e}"
    except Exception as e: 
        return f"Error {e}"
    else: #se ejecuta si pude hacer el try
        print("Pude dividir")
        return resultado
    finally:  #se ejecuta siempre al final
        print("Ya termine")


c=dividir(4,2)
print(c)
c=dividir(2,4)
print(c)
c=dividir(4,0)
print(c)
c=dividir(4,"a")
print(c)
print("-"*90)
c=dividir2(4,2)
print(c)
c=dividir2(2,4)
print(c)
c=dividir2(4,0)
print(c)
c=dividir2(4,"a")
print(c)