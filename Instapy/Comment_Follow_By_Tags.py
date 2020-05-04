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
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_like(["droug", "dead"])

    #Damoes los parametros de que puede seguir
    session.follow_by_tags(["fit", "fitness", "cute", "chad", "gains", "4Chan", "GigaChad", "natty", "steroids"], amount=5)

    #Activamos la funcion de seguir en un porcentaje de 100%
    session.set_do_follow(enabled=True, percentage=100)

    photo_comments = ['Nice bro!',
                     'Very nice!',
                     'Good',
                     'Cool',
                     'Very interesting',
                     'Nice',
                     'Interesting',
                     'Nice job']

    #Activamos la funcion de dar comentarios en un porcentaje de 100%
    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(photo_comments, media='Photo')
    session.join_pods(topic='fitness', engagement_mode='no_comments')