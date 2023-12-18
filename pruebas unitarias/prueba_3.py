#Dado un valor de potencia activa(W) y reactiva (VAr) crear una clase que calcule la potencia 
#aparente (VA) sin considerar potencia de distorsión debida a armónicas. Si no está familiarizado
#con conceptos eléctricos, matemáticamente el módulo se reduce al teorema de Pitágoras, y el ángulo
#se reduce al teorema del coseno. 
import math

class potencia_va:
    def __init__(self, p_activa, p_reactiva):
        self.activa=p_activa
        self.reactiva=p_reactiva
        self.aparente=math.sqrt((self.activa**2)+(self.reactiva**2))
        self.angulo=math.cos(self.reactiva/self.activa)

    def __str__(self):
        return f"Módulo={self.aparente:.3f}VA ángulo={self.angulo:.3f}rad"

print(potencia_va(5,24))

print(potencia_va(8,15))

print(potencia_va(3,-32))