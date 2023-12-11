class Etiquetas:

    def __init__(self):
        self.contador = 0

    def next_etiqueta(self):
        etiqueta = f'l{self.contador}'
        self.contador += 1
        return etiqueta