class cuadrado:
    def __init__(self,lado,color):
        self.lado=lado
        self.superficie=lado**2
        self.perimetro=lado*4
        self.color=color
    def saludar(self):
        print(f"Hola,soy un cuadrado de {self.lado}cm de lado")

mi_cuadrado=cuadrado(lado=6, color="blanco")

print(f"La superficie de tu cuadrado es: {mi_cuadrado.superficie}")
print(f"El color de tu cuadrado es: {mi_cuadrado.color}")
print(type(mi_cuadrado))
mi_cuadrado.saludar()