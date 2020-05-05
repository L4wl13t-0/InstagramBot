# Importamos las librerias necesarias
from instapy import InstaPy
from instapy import smart_run

# Creamos las variables que guarda la cuenta
insta_username = 'jokael_nimerrs'
insta_password = 'houkai'

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

    session.story_by_users(['darwinuzcategui1973', 'darwinuzcategui1973'])
