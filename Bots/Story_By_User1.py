# Importamos las librerias necesarias
from instapy import InstaPy
from instapy import smart_run
from instapy_cli import client

from pymongo import MongoClient


# buscar los datos en la base de datos
client = MongoClient()

db = client.botsinstaPydb

# coleccion o tablas de la base datos
usuariosDb = db.users


# def get_story_by_users():
#    datos = []
#    story_users = storyUsuarios.find()
#    for dat in story_users:
#        datos.append({dat["story_by_users"]})
#    # print(datos)
#    return list(datos)


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
# story_by_users = str(get_story_by_users())
# story_by_users = story_by_users.replace("{", "")
# story_by_users = story_by_users.replace("}", "")
# story_by_users = story_by_users.replace("[", "")
#  story_by_users = story_by_users.replace("]", "")
# story_by_users = story_by_users.replace("'", "")

usuarios = get_users()  # realizamos la lista de usuarios
# hacemos el ciclo para colocar todos los 1000 o X usuarios
for unUser in usuarios:

    # aqui el codigo para subir imagen
    insta_img = 'img.jpg'
    insta_txt = 'esta mi mi imagen'

    insta_username = unUser['insta_username']  # 'darwinjosejosepedro'
    insta_password = unUser['insta_password']  # 'Clave321**'
    # insta_username = 'jokael_nimerrs'
    # insta_password = 'houkai'

    # creamos la variable donde se almacena e inicia la cuenta
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False)

    # Definicmos la funcion que inicia la cuenta
    with smart_run(session):
        #client.upload(insta_img, insta_txt)

        # Damos los parametros de la cuenta
        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=4000,
                                        min_followers=0,
                                        min_following=0)

        session.set_do_story(enabled=True, percentage=95, simulate=True)

        # session.story_by_users(story_by_users)
        session.story_by_users(["darwinjosejosepedro"])
