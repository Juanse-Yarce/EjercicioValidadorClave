# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod 


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada):
        self._longitud_esperada = _longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada
    
    

        

