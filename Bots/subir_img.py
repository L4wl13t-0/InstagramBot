# Importamos las librerias necesarias

from instapy_cli import client
from pymongo import MongoClient


# buscar los datos en la base de datos
clientM = MongoClient()

db = clientM.botsinstaPydb

# coleccion o tablas de la base datos
usuariosDb = db.users


def get_users():
    datos = []
    users = usuariosDb.find()
    for dat in users:
        datos.append({
            "insta_username": dat["username"],
            "insta_password": dat["password"]
        })
    # print(datos)
    return datos


# Creamos las variables que guarda la cuenta este lo vamos a tomar desde otra tabla o coleccion

usuarios = get_users()  # realizamos la lista de usuarios
# hacemos el ciclo para colocar todos los 1000 o X usuarios
for unUser in usuarios:

    # aqui el codigo para subir imagen

    insta_username = unUser['insta_username']  # 'darwinjosejosepedro'
    insta_password = unUser['insta_password']  # 'Clave321**'
    # insta_username = 'jokael_nimerrs'
    # insta_password = 'houkai'

    # creamos la variable donde se almacena e inicia la cuenta
    insta_img = 'img.jpg'
    insta_txt = 'esta mi mi imagen'

    with client(insta_username, insta_password) as cli:
        cli.upload(insta_img, insta_txt)
