#Importamos las librerias necesarias
from instapy import InstaPy
from instapy import smart_run

#Creamos las variables que guarda la cuenta
insta_username = ''
insta_password = ''

#creamos la variable donde se almacena e inicia la cuenta
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

#Definicmos la funcion que inicia la cuenta
with smart_run(session):

    #Damos los parametros de la cuenta
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4000,
                                    min_followers=2,
                                    min_following=2)

    session.set_dont_like(["droug", "dead"])

    #Activamos la funcion de seguir en un porcentaje de 90%
    session.set_do_follow(enabled=True, percentage=90)

    #Damos los parametros de que puede comentar
    session.set_comments(['Nice bro!',
                          'Very nice!',
                          'Good',
                          'Cool',
                          'Very interesting',
                          'Nice',
                          'Interesting',
                          'Nice job'], media='Photo')

    #Activamos la funcion de dar comentarios en un porcentaje de 90%
    session.set_do_comment(enabled=True, percentage=90)

    #Activamos la funcion de dar like en un porcentaje de 90%
    session.set_do_like(enabled=True, percentage=90)

    session.interact_by_users(['', ''], amount=5, randomize=True, media='Photo')