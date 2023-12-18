#definir una clase que tenga un método volumen() que me devuelva el volúmen de un rectángulo

class rectangulo: 
    def __init__(self, b, a, p):
        self.b=b
        self.a=a
        self.p=p
    
    def volumen(self):   
        return self.a * self.b * self.p 
    
rect=rectangulo(10,5,8)
print(rect.volumen())

rect=rectangulo(9,4,3)
print(rect.volumen())

rect=rectangulo(30,6,2)
print(rect.volumen())