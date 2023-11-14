class Animal:

    especie = "No definida"

    def __init__(self, nombre):
        self.xx = nombre
        self.__zz = nombre 

    def __saludar(self):
        print(f"hola soy {self.__zz} y estoy contento!")

    def _presentarse(self):
        self.__saludar()
        print("Ya llegué")



animal = Animal("pedro")

print(animal.especie)
print(animal.xx)
#print(animal.__zz) #esta bien que de error, es para que el que ejecuta no pueda acceder, es privada desde afuera
#print(animal.__saludar()) #da error porque no me deja acceder de afuera por el __
animal._presentarse()#no puedo acceder a saludar de afuera, pero presentarse sí