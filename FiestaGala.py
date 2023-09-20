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
         _costeF_Persona = 400

    def get_costeF_Persona(self):
        costo_fiesta = super().calcular_costo()
        #tomar el calculo de super clase
        #sumarlo al calculo de la fiesta de gala
        gala = self.get_costeF_Persona * super().get_numero_persona()
        total = costo_fiesta + gala
        return self._costoF_Persona

