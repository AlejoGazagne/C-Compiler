from abc import ABC

class ID(ABC):
    def __init__(self, nombre, tDato, inicializado = False, accedido = False):
        self._nombre = nombre
        self._tDato = tDato
        self._inicializado = inicializado
        self._accedido = accedido
        
    @property
    def nombre(self):
        return self._nombre

    @property
    def tDato(self):
        return self._tDato

    @property
    def inicializado(self):
        return self._inicializado

    # @property
    # def accedido(self):
    #     return self._accedido

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @tDato.setter
    def tDato(self, tDato):
        self._tDato = tDato

    @inicializado.setter
    def inicializado(self, inicializado):
        self._inicializado = inicializado

    #@accedido.setter
    def setAccedido(self):
        self._accedido = True
        
class Variable(ID):
    pass
    
class Funcion(ID):
    def __init__(self, nombre, tDato, args):
        super().__init__(nombre, tDato)
        self._args = list(args)
        
    @property
    def args(self):
        return self._args