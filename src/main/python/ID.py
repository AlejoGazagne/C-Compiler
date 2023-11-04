from abc import ABC, abstractmethod

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

    @property
    def accedido(self):
        return self._accedido

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @tDato.setter
    def tDato(self, tDato):
        self._tDato = tDato

    @inicializado.setter
    def inicializado(self, inicializado):
        self._inicializado = inicializado

    @accedido.setter
    def accedido(self, accedido):
        self._accedido = accedido
        
class Variable(ID):
    pass
    
class Funcion(ID):
    def __init__(self, nombre, tDato, args, inicializado = False, accedido = False):
        super().__init__(self, nombre, tDato)
        self._args = list(args)
        
    @property
    def args(self):
        return self._args