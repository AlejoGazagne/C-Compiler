from ID import *
from Contexto import *

class TS():
    
    _ctx = []
    _instancia = None
    
    def __init__(cls): 
        if TS._instancia is None:
            TS._instancia = object.__init__(cls)
            TS._ctx.append(Contexto())
        return TS._instancia
    
    def buscarLocal(self, id):
        if id in TS._ctx[-1].simbolos:
            return TS._ctx[-1].simbolos
    
    def buscar(self, id):
        for contexto in TS._ctx[-1::-1]:
            if id in contexto.simbolos:
                return contexto
        
    def agregar(self, id):
        TS._ctx[-1].agregarSimbolo(id)
        
    def agregarContexto(self, ):
        TS._ctx.append(Contexto())
        
    def borrarContexto():
        TS._ctx[-1].pop()
    