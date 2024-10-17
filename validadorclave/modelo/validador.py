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

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            return False
            
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, _longitud_esperada):
        super().__init__(_longitud_esperada)

    def contiene_caracter_especial(self, clave):
        cracteres_especiales = "@_#$%"
        if not any(c in cracteres_especiales for c in clave):
            return False

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, _longitud_esperada):
        super().__init__(_longitud_esperada)

    def contiene_calisto(self, clave):
        if clave.lower().count("calisto") == 0 or clave.upper().count("CALISTO") < 2:
            return False
   

        

