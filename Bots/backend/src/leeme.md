# Guia para Utilizar el **Backend**

1. Hay que instalar inicialmente la base de datos mongodb (https://www.mongodb.com/download-center/community)

1. sieguiente paso instalar las dependencia para trabajar en el EN SCRIPS DE BACKEND app.py.
   pip install Flask
   pip install flask-Pymongo
   pip install Flask-Cors

1. herraminetas a intalar para realizar Test.:

   #### Postman (https://www.postman.com/) se utilizar como un cliente apara leer api Restfull

   #### Robo3t (https://robomongo.org/download) se utiliza como un cliente para leer basedatos mongodb

1. En la carpeta Bots\backennd\src\ ... aqui se encuentra el scrip que tiene el backend para crear las api de la base datos mongodb.
1. En momento que se tiene todo instalado. y corriendo el servicio de mongodb en localhost.
1. se Ejecuta el scrip Bots\backennd\src\app.py
   esto si estas, en la carpeta src
   python app.py
   ahora si esta en la carpeta backend
   python src\app.py
   si todo esta bien saldra en la consola esto datos"
   Use a production WSGI server instead.

   _Debug mode: on_
   _Restarting with stat_
   _Debugger is active!_
   _Debugger PIN: 203-558-319_
   _Running on Use a production WSGI server instead.
   Debug mode: on
   Restarting with stat
   Debugger is active!
   Debugger PIN: 203-558-319
   Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) (Press CTRL+C to quit)_

1. Ahora te coloca en la ruta http://127.0.0.1:5000/ si ejecuta esta ruta raiz tu servidor de base datos ya esta corriendo y en el navegador sale:

   ## Hola Base datos

1. Por Ultimo ahora debera cargas los datos de los scrip en la base datos.
1. Ejecute postman y la opcion de untited request coloque por metodo get esta ruta para ver la lista de los usuarios GET
   http://localhost:5000/users
   te saldra la lista de usuarios ,
   pero como es la primera vez te va salir una lista vacia
   para cargar los usuarios coloca por el metodo POST ESTA RUTA
   http://localhost:5000/users
   alli debera hacer dos configuraciones basicas de cualquier formulario de servidoes.
   la primera en la opcion de headers en campo key colocar Content-Type y value application/json.
   ya con esto tiene configurado la cabecera de tu frontend.
   para terminar en la opcion body en raw JSON , carga un json
   valido para grabar los datos en la base de datos ejemplo
   {
   "username": "miUsuario",
   "password": "Clave321"
   }
   y pulsa en en boton de send o enviar si todo esta bien
   te va salir este resultado o parecido
   {
   "\_id": "5eb70164f96a2741ed886ca9",
   "password": "Clave3ss21\*\*",
   "username": "darwinsssjosejosepedro"
   }
   esto quiere decir que ya grabo el primer usuario en la lista.
   tambien puede ver la coleccion de datos en mongo3t

la otra ruta para cargar los tag
por el metodo POST

http://localhost:5000/tags
en la opcion body en raw JSON , carga un json
valido para grabar los datos en la base de datos ejemplo

{
"tag": "pelicula"
}

el resultrado al pulsar send
es parecido a esto
{
"\_id": "5eb70208f96a2741ed886caa",
"tag": "pelicula"
}

ya para ver si cargaste todos los tags
la ruta es por metodo GET
http://localhost:5000/tags
Se visualiza todos los tags cargado en la base de datos
como este ejm.
[
{
"id": "5eb3fe24e5e63ae8d032e671",
"tag": "kotlin"
},
{
"id": "5eb3fe4be5e63ae8d032e672",
"tag": "python"
},
{
"id": "5eb3ff6cddaa3195d2d355cb",
"tag": "java"
},
{
"id": "5eb3ffad14deeb5795ea826c",
"tag": "C#"
},
{
"id": "5eb40032e903e4e8e7f23e93",
"tag": "c++"
},
{
"id": "5eb4006ccef784d56392eba6",
"tag": "javascrip"
},
{
"id": "5eb410252b877230b9de68a6",
"tag": "flutter"
},
{
"id": "5eb410382b877230b9de68a7",
"tag": "developer"
},
{
"id": "5eb410482b877230b9de68a8",
"tag": "programacion"
},
{
"id": "5eb70208f96a2741ed886caa",
"tag": "pelicula"
}
]

##### finn......
