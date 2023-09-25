from Fiesta import Fiesta

class FiestaCumple(Fiesta):
    
    def __init__(self,numero_persona):
        super().__init__(numero_persona)
        self.__valueCake = 0 
        self.__textCake = ""
    
    def personalizar_pastel(self,texto:str):
        self.__textCake = texto

    def calcular_costo(self):
        #llamar a calcular costo de super clase
        #sumarlo a los costo de una fiesta de cumpleanio
        fiesta = super().calcular_costo()
        cumple = self.__valueCake
        total = fiesta + cumple
        return total
    
    

    def calcular_costo_pastel(self):
        if self.__textCake!="":
            if super().get_numero_personas()<=4:
                self.__valueCake = 5000
            else:
                self.__valueCake = 10000