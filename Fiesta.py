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
                self.__costo_decoracion = self.__numero_persona * 16000
    
    def calcular_costo(self):
        #deberia sumarse los costo de ubna fiesta y retornar
        #costo comida es igual a 3500 x Numero persoba
        costo_comida = self.__costo_comida_persona * self.__numero_personas
        costo = self.__costo_decoracion + costo_comida + self.__bono_extra
        return costo

    def get_numero_persona(self):
        return self.__numero_persona

    def __str__(self):
        txt = f"numero persionba: {self.__numero_persona}"
        txt += f"\nCosto decoracion {self.__costo_decoracion}"
        #Agregar todoo lo que quieras mostrar
        return txt