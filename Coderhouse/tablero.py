class Tablero:

    base = 8
    altura = 8

    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida

    def imprimir(self):
        

    def __str__(self):
        return f"Tablero: <entrada> {self.entrada} <salida> {self.salida}"