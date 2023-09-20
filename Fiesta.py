class Fiesta:
    def __init__(self, numero_personas):
        self.__numero_persona = numero_personas
        self.__costo_decoracion = 0
        if numero_personas > 12:
            self.__bono_extra = 10000
        else:
            self.__bono_extra = 0

        self.__costo_comida_persona = 3500
        self.__decora = False

    def calcular_costo_decoracion(self,decora:bool):
        if decora:
            if self.__numero_persona>20:
                self.calcular_costo_decoracion = self.__numero_persona * 22000
            else:
                self.__costo_decoracion = self.__numero_persona ^ 16000