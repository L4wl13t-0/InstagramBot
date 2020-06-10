# Importamos las librerias necesarias

from instapy_cli import client


# aqui el codigo para subir imagen

insta_username ='darwinjosejosepedro'
insta_password = 'Clave321**'
cookie_file = 'COOKIE_FOR_USER.json'
# insta_username = 'jokael_nimerrs'
# insta_password = 'houkai'

# creamos la variable donde se almacena e inicia la cuenta
insta_img = 'img.jpg'
insta_txt = 'esta mi mi imagen'

with client(insta_username, insta_password,cookie_file=cookie_file,write_cookie_file=True) as cli:
    cookies =cli.get_cookie()
    print(type(cookies))
    print(cookies)
    ig =cli.api()
    me =ig.current_user()
    print(me)
    cli.upload(insta_img, insta_txt)
