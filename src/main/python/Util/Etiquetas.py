class Etiquetas:
    funciones = dict()
    _contador = 0

    def next_etiqueta(self):
        etiqueta = f'l{self._contador}'
        Etiquetas._contador += 1
        return etiqueta
    
    def etiqueta_funcion(self, identificador):
        # si el identificador existe, me devuelve la lista de etiquetas
        for id in Etiquetas.funciones:
            if str(id) == str(identificador):
                return Etiquetas.funciones[id]
        # si el identificador no existe, debo generar las etiquetas para la funcion
        list = []
        etiqueta1 = Etiquetas.next_etiqueta(self)
        etiqueta2 = Etiquetas.next_etiqueta(self)

        list.append(etiqueta1)
        list.append(etiqueta2)

        Etiquetas.funciones[identificador] = list
        return list