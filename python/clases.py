from clases_secundario import AutoDeportivo







class Auto():
    color = "verde"
    # modelo = "toyota"
    # precio = 1

    def __init__(self, modelo, precioNuevo):
        self.modelo = modelo
        self.precioNuevo = precioNuevo
        self.saludar()

    def saludar(self):
        print("Hola clase Auto")

    def acelerar(self):
        print("acelerando:", self.modelo)
        self.modelo = "toyoya 2019"
        print(self.modelo)

    def frenar(self, velocidad):
        self.aceleracion = "40 metros/m"
        self.acelerar()

        if velocidad > 100:
            print("frenar!!!!")
            return True
        return False

    # def privadoAuto(version):
    #     print(version)



class Autodromo(Auto, AutoDeportivo):

    def __init__(self):
        print("init clase AutoDronomo")
        Auto.__init__(self, "tesla204", 345)
        AutoDeportivo.__init__(self)
    
    # def empezarCarrera(self):
    #     # Auto.__init__(self, "tesla204", 345)
    #     print("iinicar competencia")


# autoToyota = Auto("Tesla", 123 )

# print(autoToyota.color)
# print(autoToyota.modelo)
# print(autoToyota.precio)
# autoToyota.color = "red"
# autoToyota.modelo = "Toyota 2024"
# print(autoToyota.color)
# print(autoToyota.modelo)

# autoToyota.acelerar()

# print(autoToyota.modelo)

# salidaFrenar = autoToyota.frenar(120)
# print(salidaFrenar)

# print(autoToyota.aceleracion)

# autoToyota.privadoAuto("version1")

# print(autoToyota.precioNuevo)
# print(autoToyota.modelo)



Autodromo2024 = Autodromo()

print(Autodromo2024.color)
print(Autodromo2024.color)
Autodromo2024.frenar(123)

Autodromo2024.empezarAutoSport()