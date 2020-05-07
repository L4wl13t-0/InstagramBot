# Importamos las librerias necesarias
from instapy import InstaPy
from instapy import smart_run
from pymongo import MongoClient


# buscar los datos en la base de datos
client = MongoClient()

db = client.botsinstaPydb

# coleccion o tablas de la base datos
usuarios1 = db.users
tages = db.tags


def get_tags():
    datosTag = []
    tag = tages.find()
    for unTag in tag:
        datosTag.append({unTag["tag"]})
        # print(unTag)

    return datosTag


def get_users():
    datos = []
    users = usuarios1.find()
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

usuariosLista = get_users()  # realizamos la lista de
tagsLista = get_tags
# print(tagsLista)
# hacemos el ciclo para colocar todos los 1000 o X usuarios
for unUser in usuariosLista:

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

        # Damos los parametros de la cuenta
        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=4000,
                                        min_followers=45,
                                        min_following=77)

        session.set_dont_like(["droug", "dead", "Sexi"])

        # Damoes los parametros de que puede seguir
        # session.follow_by_tags(["programming", "hacking", "technology","baskeball", "jum", "futbol"], amount=5)
        # print(tags)
        session.follow_by_tags(tags=tagsLista, amount=5)

        # Activamos la funcion de seguir en un porcentaje de 100%
        session.set_do_follow(enabled=True, percentage=100)

        photo_comments = ['Nice bro!',
                          'Very nice!',
                          'Good',
                          'Cool',
                          'Very interesting',
                          'Nice',
                          'Interesting',
                          'Nice job']

        # Activamos la funcion de dar comentarios en un porcentaje de 100%
        session.set_do_comment(enabled=True, percentage=95)
        session.set_comments(photo_comments, media='Photo')
        session.join_pods(topic='technology', engagement_mode='no_comments')
