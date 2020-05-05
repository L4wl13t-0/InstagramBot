# Importamos las librerias necesarias
from instapy import InstaPy
from instapy import smart_run

from pymongo import MongoClient


# buscar los datos en la base de datos
client = MongoClient()

db = client.botsinstaPydb

# coleccion o tablas de la base datos
usuarios = db.users


def get_story_by_users():
    datos = []
    users = usuarios.find()
    for dat in users:
        datos.append({dat["story_by_users"]})
    # print(datos)
    return list(datos)


def get_users():
    datos = []
    users = usuarios.find()
    for dat in users:
        datos.append({
            "insta_username": dat["username"],
            "insta_password": dat["password"]
        })
    # print(datos)
    return datos[0]


# Creamos las variables que guarda la cuenta
story_by_users = str(get_story_by_users())
story_by_users = story_by_users.replace("{", "")
story_by_users = story_by_users.replace("}", "")
story_by_users = story_by_users.replace("[", "")
story_by_users = story_by_users.replace("]", "")
story_by_users = story_by_users.replace("'", "")

print("probando que visualizar los datos de la base datos")
print(story_by_users)


# insta_username = 'jokael_nimerrs'
# insta_password = 'houkai'

usuarios = get_users()
insta_username = usuarios['insta_username']  # 'darwinjosejosepedro'
insta_password = usuarios['insta_password']  # 'Clave321**'


# creamos la variable donde se almacena e inicia la cuenta
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

# Definicmos la funcion que inicia la cuenta
with smart_run(session):

    # Damos los parametros de la cuenta
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4000,
                                    min_followers=2,
                                    min_following=2)

    session.set_do_story(enabled=True, percentage=95, simulate=True)

    session.story_by_users(story_by_users)
    # session.story_by_users(['cristiano', 'jumpman23', 'noah_bellhat', "david_braham00"])
