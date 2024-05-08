


def acelerarMoto(modelo, pilotos):
    print("acelerando..", modelo)
    
    if modelo == "yamaha":
        print("acelear yamaha 100kmxh")
    
    for pilot in pilotos:
        print( f"el piloto se llama {pilot.upper()}" )

    return True


def saludar(nombre="jorge"):
    print("hola mundo en python", nombre)


# saludar()

pilotos = ["mario", "henry", "jaime"]

acelracion =  acelerarMoto("yamaha", pilotos)
print(acelracion)
