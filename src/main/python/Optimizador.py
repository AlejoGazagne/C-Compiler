import re

class Optimizador:

    def optimizar():

        with open("output/CodigoIntermedio.txt", "r") as archivo:
            # lineas = archivo.readlines()
            contenido = archivo.read()
        
        #limpio los valores de la lista
        # for i in range(len(lineas)):
        #     lineas[i] = lineas[i].strip("\n").split()
            
        # Iterar sobre cada sublista en la lista de listas

        #PRIMERA PASADA, REEMPLAZO TEMPORALES CON UNA SOLA ASIGNACION, POR VARIABLE = VALOR (se complica)   
        pattern = re.compile(r'(t\d+)\s*=\s*(.*)(?!\s*[+/*><-])\n(.*)\s*=\s*(t\d+)(?!\s*[+/*><-])')
        valores = re.findall(pattern, contenido)

        #patron = "(.*) = (.*)\n"
        # patron = re.compile(r't\d+\s*=\s*(.*)\n(\w+)\s*=\s*t\d+([^+\-*/])')
        # valores = re.findall(patron, contenido)
        # print("Valores ")
        # print(valores)
        for val in valores:
           contenido = re.sub(pattern, f'{val[2]} = {val[1]}' ,contenido, 1) 
        # print(contenido)
        # pattern = re.compile(r'\bt\d+\s*=\s*(\d+)\nt\d+\s*=\s*(\d+)\n(.*)\s*=\s*t\d+\s*([+/*-])\s*t\d+\b')
        # valores = pattern.findall(contenido)
        # for value in valores:
        #     operacion = value[0] + value[3] + value[1]
        #     operado = eval(operacion)        
        #     contenido = re.sub(pattern, f'{value[2]} = {operado}', contenido, 1)
        
        #SEGUNDA PASADA, REEMPLAZO TEMPORAL CON OPERACIONES DE TEMPORALES, POR VARIABLE = OPERACION (se complica)
        #patron = "t\d+ = (t\d+ [+-/*] t\d+)\n(.*) = t\d+"
        #valores = re.findall(rf'{patron}', contenido)
        #print(valores)
        
        
        #TERCERA PASADA, REEMPLAZO TEMPORAL CON OPERACION DE NUMERO, POR VARIABLE = RESULTADO (me canse xd)
        #patron = "t\d+ = \d+ [+-/*] \d+\n(.*) = t\d+"
        #valores = re.findall(patron, contenido)
        #print(valores)
        
        
        with open("output/CodigoIntermedioOptimizado.txt", "w+") as optimizado:
            optimizado.write(contenido)
        
        archivo.close()
        optimizado.close()
        
        