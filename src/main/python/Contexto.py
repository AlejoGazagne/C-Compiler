class Contexto():
    
    def __init__(self, **kwargs):
        self._simbolos = kwargs
        
    @property
    def simbolos(self):
        return self._simbolos
    
    def agregarSimbolo(self, id):
        self._simbolos[id.nombre] = id