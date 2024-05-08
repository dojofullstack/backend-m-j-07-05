

# comentario en linea

"""
    comentarios
    de
    multiples
    lineas
"""

"""
    Tipo de dato String
"""

usuario = "\n   erick erick  \n"
# print(type(usuario))
# print(dir(usuario))

# print(usuario.find("ck"))

# print(usuario.count("erick"))

# print(usuario.title())

# print(usuario.replace("ck", "@gmail.com"))

# print(usuario.index("ick"))

# print(usuario.startswith("ick"))
# print(usuario.endswith("ick"))

# print(usuario.strip())
# # print(usuario)

# print(usuario.isnumeric())

# # isnumeric

# puntaje = 123
# print(str(puntaje))


"""
    Tipo de dato Numerico
"""

puntajeEncuesta = 123
precio = 9.5

print(puntajeEncuesta)
print(type(puntajeEncuesta))
print(type(precio))

# print(puntajeEncuesta + 10)
# print(puntajeEncuesta - 2)
# print(puntajeEncuesta * 3)
# print(puntajeEncuesta / 2)

# puntajeEncuesta = puntajeEncuesta + 10
# puntajeEncuesta += 10
# print(puntajeEncuesta)

# print(int("123"))
# print(float("5.7") * 2)

# print(int("123" ) + 34)


"""
    Tipo de dato Bool
"""

isAdmin = True
isLogin = False

# print(isAdmin)
# print(type(isAdmin))
# print(isLogin)
# bool()


"""
    Tipo de dato Listas
"""

frutas = ["manzanas", "fresas", "banano", "cieurlas" ]

verduras = ["apio", "tomate", "espincas"]

# print( len(frutas) )

# print(dir(frutas))

# frutas.append(123)
frutas.append("kiwi")

# frutas.clear()
frutasCopy =  frutas.copy()

# print(frutasCopy)

# conteo = frutas.count("kiwi")
# print(conteo)

# frutas.extend(verduras)


# frutas.pop()

# frutas.remove("tomate")


# frutas.sort()

# print(frutas)

# print(list("henry"))


"""
    Tipo de dato dictionario
"""

perfil = {
    "email": "user@gmail.com",
    "id": 3,
    "name": "pedro"
}
# print(perfil)
# print(type(perfil))

# print(dir(perfil))

#CRUD
# print(perfil["id12"])
# email = perfil.get("config", "no existe")

# perfil["color"] = "verde"

# perfil["id"] = 9

# del perfil["id"]



# print(perfil.keys())
# print(perfil.values())

# perfilAdmin = {
#     "admin": True,
#     "isLogin": False
# }

# perfil.update(perfilAdmin)

# print(perfil)

dict()


"""
    Tipo de dato set o conjuntos
"""

# productos = {"samsung", "iphone", "xiomi", "xiomi"}
# productos2 = {"samsung", "pocox"}
# print(productos.intersection(productos2))
# # print(dir(productos))
# productos.add("LG")
# print(productos)

# set(listaEmails)


#- tuplas
# una tupla es un lista de elementos inmutables

TokenApi = ("pk-login", "pk-01029109201")
print(TokenApi)
# print(dir(TokenApi))

print(TokenApi[0])
print(TokenApi[1])
print(TokenApi.count("pk-01212"))
# print(TokenApi.index("pk-login-10920912"))


print(TokenApi)
print(list(TokenApi))

tuple()


usuario = None
#null 