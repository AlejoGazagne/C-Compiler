class Contexto():
    
    def __init__(self, **kwards):
        self._simbolos = kwards
        
    @property
    def simbolos(self):
        return self._simbolos
    
    def agregarSimbolo(self, identificador):
        self._simbolos[identificador.nombre] = identificador