

""" condicionales """

usuarioEnroll = False

# if usuarioEnroll:
#     print("usuario enrrollado")
#     email = "dojo@gmail.com"
#     print(email)
#     if email == "jose@gmail":
#         pass
# else:
#     print("usuario no registrado.")


""" condicionales multiples anidadada"""


miembroPremium = False
nombreMiembro = "david"

# if miembroPremium:
#     print("es miembro dar acceso")
# elif nombreMiembro == "jose":
#     print("jose si es miembro")
# elif nombreMiembro == "david":
#     print("david si es miembro")
# else:
#     print("no hay miembros")




## ejempo codigo javascript
# if (operacion) {
#  //code
# } else if (evalular){

# }


""" operadores logicos """
# operador logico OR  || "or"
# operador logico AND  && "and"
# operador de negacion NOT !  "not"


# series = ["batman", "pokemon", "big bang theory"]
# seriePreferida = "pokemon"

# if len(series) >= 3 and seriePreferida == "pokemon":
#     print("genial las series de pokemnon")


# if len(series) >= 3 or seriePreferida == "la casa de papel":
#     print("genial la serie!!")


# if not seriePreferida:
#     print("no hay serie")
# else:
#     print("ver documentales")




""" ciclos en Python """

# iterador for
frutas = ["fresas", "mango", "uvas", "sandias"]

# for fruty in frutas :
#     print(fruty)

# for (index, fruta) in enumerate(frutas) :
#     # print(frutas.index(elemento))
#     print(index, fruta)


# for numero in range(10):
#     print(numero)


""" los breakpoint siempre puedes aplicarlos en los ciclos for y while
 continue y el
 break
"""

# ciclo while

isMonitorActive = True

while isMonitorActive:
    print("iterando hacia el infinito")
    respuesta = input("quiere salir de ciclo while??")

    if respuesta == "si":
        print("cerrar while")
        break
    else:
        print("continuar hacia el infigito..")



print("final de la App")