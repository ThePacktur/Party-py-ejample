from Fiesta import Fiesta

class FiestaGala(Fiesta):

    #constructor 
    def __init__(self,numero_personas):
        super().__init_(numero_personas)
        self.__costeF_Persona = 2000
        self.__opcion_saludable = False

    def set_opcion_saludable(self,opcion_saludable:bool):
        self.__opcion_saludable = opcion_saludable
        if opcion_saludable:
         self.__costeF_Persona = 4000

    def costeF_Persona(self):
        costo_fiesta = super().calcular_costo()
        #tomar el calculo de super clase
        #sumarlo al calculo de la fiesta de gala
        gala = self.__costeF_Persona * super().get_numero_persona()
        total = costo_fiesta + gala
        return total

    def __str__(self):
       txt = super().__str__()
       txt += f"\nCosto fijo Persona: {self.__costeF_Persona}"
       #Agregar los Atributos a mostrar de la fista gala
       return txt