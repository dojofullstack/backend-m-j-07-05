import requests
import json


def obtenerSeguidoresInstagram(perfilUrl):
    print(f"ingresar al sitio web {perfilUrl}")
    print("obtener seguidores")

    data = requests.get(perfilUrl)
    # print(data.text)
    fichero = open("./index.html", "w")
    fichero.write(data.text)
    fichero.close()




def getUsers(api):
    print(f"get api users {api}")
    data = requests.get(api)
    dataJson = data.json()
    # print(dataJson["users"][0])
    fichero = open("./data.json", "w")
    fichero.write(json.dumps(dataJson))
    fichero.close()


def loginInit(username, password):
    api = "https://dummyjson.com/auth/login"
    print(f"login init")
    credenciales = {
        "username": username,
        "password": password,
    }
    data = requests.post(api, json=credenciales)
    dataJson = data.json()
    print(dataJson["id"])

# obtenerSeguidoresInstagram("https://www.instagram.com/luisitocomunica/?hl=es-la")
# getUsers("https://dummyjson.com/users")

loginInit("kminchelle", "0lelplR")