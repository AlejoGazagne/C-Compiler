from ID import *
from Contexto import Contexto

class TS():
    
    _pilaCtx = []
    _instancia = None
    
    def __init__(cls): 
        if TS._instancia is None:
            TS._instancia = object.__init__(cls)
            TS._pilaCtx.append(Contexto())
        return TS._instancia
    
    def buscarLocal(self, id):
        if id in TS._pilaCtx[-1].simbolos:
            return TS._pilaCtx[-1].simbolos
    
    def buscar(self, id):
        for contexto in TS._pilaCtx[-1::-1]:
            if id in contexto.simbolos:
                return contexto
            
    def buscarGlobal(self, id):
        if id in TS._pilaCtx[0].simbolos:
            return TS._pilaCtx[0]
        
    def agregar(self, id):
        TS._pilaCtx[-1].agregarSimbolo(id)
        
    def agregarContexto(self):
        TS._pilaCtx.append(Contexto())
        
    def borrarContexto(self):
        TS._pilaCtx.pop()
    
    def actualizar(self, id):
        TS.buscar(TS, id.nombre).agregarSimbolo(id)
    
    def getContextos(self):
        return TS._pilaCtx