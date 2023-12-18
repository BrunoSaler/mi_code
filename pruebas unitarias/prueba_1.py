# verificar si un número es primo

def primo(x):
    try:
        for i in range(2, x):
            if x % i == 0:
                return "No es Primo"
        return("Es Primo")
    except TypeError:
        return("No es numérico")
    

print(primo(7))
print(primo(54))
print(primo("abc"))