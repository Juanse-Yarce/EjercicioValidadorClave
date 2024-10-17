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
    
    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            return False
        
    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            return False

    
        

