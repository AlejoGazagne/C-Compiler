from ID import *
from TS import *

class Utilidades:
    @staticmethod
    def getArgsFuncion(argumentos):
        argumentos = argumentos.split("(")[1].split(")")[0].split(",")
        listArgs = []
        
        for arg in argumentos:
            if arg[:3] == "int":
                nombreVar = arg[3:]
                tDatoVar = int
                listArgs.append(Variable(nombreVar, tDatoVar))
            elif arg[:6] == "double":
                nombreVar = arg[6:]
                tDatoVar = "double"
                listArgs.append(Variable(nombreVar, tDatoVar))
            elif arg == "":
                print("lista de argumentos vacia")
                
        return listArgs
        
    @staticmethod
    def verificarPrototipoFuncion(identificador):
        ctxGlobal = TS._ctx[0].simbolos 
        for i in ctxGlobal:
            if(identificador.nombre == i):
                id = ctxGlobal[i]
                break
        if identificador == id:
            return True
