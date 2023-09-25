from Fiesta import Fiesta
from FiestaCumple import FiestaCumple
from FiestaGala import FiestaGala

def menu():
    opcion: "n"
    while opcion!='n':
        print("Bienvenido")
        print("vas a organuzar una fiesta")
        print("ingrea 1 para una fiesta de gala")
        print("ingresa 2 para una fiesta de cumpleanio")
        op = input("Ingreese tuoi de fista: ")
        if op.lower()=="1" or op.lower()=="2":
            cotizarFiesta(int(op))
        else:
            print("la opcion es invalida ")
        opcion = input("Desea realizar otra opcionb: s/n")

def cotizarFiesta(opcion:int):
    if opcion == 1:
        crearFiestaGala()
    else:
        crearFiestaCumpleanio()

def crearFiestaGala():
    nPersona = int(input("Ingrese la cantidad de personas que asistiran a la fiesta: "))
    gala = FiestaGala(nPersona)
    gala.calcular_costo_decoracion(decidete("decorar"))
    gala.set_opcion_saludable(decidete("menu saludable"))
    total = gala.calcular_costo()
    print(gala)
    print(f"Total: {total}")

def crearFiestaCumpleanio():
    persona = int(input("Ingresar numero personas: "))
    cumple = FiestaCumple(persona)
    cumple.calcular_costo_decoracion(decidete("decora"))
    if decidete("Persibakuzar pastel"):
        texto = input("Ingresa texto del pastel: ")
        cumple.personalizar_pastel(texto)
        cumple.calcular_costo_pastel()
    total = cumple.calcular_costo()
    print(cumple)
    print(f"Total: {total}")

menu()

def decidete(texto:str):
    while True:
        opcion = input(f"Desea {texto}: s/n")
        if opcion.lower()=="s":
            return True
        elif opcion.lower()=="n":
            return False
        else:
            print("accion invalida")