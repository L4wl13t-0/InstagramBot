# Importamos las librerias necesarias
from instapy import InstaPy
from instapy import smart_run

# Creamos las variables que guarda la cuenta
insta_username = 'darwinjosejosepedro'
insta_password = 'Clave321**'
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

    # Damos los parametros de que puede dar like
    session.like_by_tags(["programming", "hacking", "technology",
                          "backetball", "futbol", "movil", "mobil"], amount=5)

    # Damoes los parametros de que puede seguir
    session.follow_by_tags(
        ["programming", "hacking", "Tecnology", "baskeball", "movil", "mobil"], amount=5)

    # Damos los parametros de que no puede dar like
    session.set_dont_like(["girls", "women", "sexi"])

    # Activamos la funcion de seguir en un porcentaje de 100%
    session.set_do_follow(enabled=True, percentage=100)

    # Activamos la funcion de dar comentarios en un porcentaje de 100%
    session.set_do_comment(enabled=True, percentage=100)

    # Activamos la funcion de dar like en un porcentaje de 100%
    session.set_do_like(enabled=True, percentage=100)

    # Damos los parametros de que puede comentar
    session.set_comments(["Very nice!", "Good", "Cool", "Very interesting", "Nice",
                          "Interesting", "excelente", "baskeball", "Nice job"], media='Photo')
