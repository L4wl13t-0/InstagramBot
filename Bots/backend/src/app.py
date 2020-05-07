from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS

import json

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'myawesomesecretkey'


app.config["MONGO_URI"] = "mongodb://localhost/botsinstaPydb"
mongo = PyMongo(app)

# coleccion o tablas de la base datos
db = mongo.db  # .bots

# creacion de rutas de mi api para los datos de la basedatos
@app.route("/")
def rutaPrueba():
    return "<h1>Hola Base datos</h1>"

# story_by_users
@app.route('/users', methods=['POST'])
def create_user():
    # Receiving Data
    username = request.json['username']
    password = request.json['password']

    if username and password:
        # hashed_password = generate_password_hash(password)

        id = mongo.db.users.insert(
            # {'username': username, 'password': hashed_password}
            {'username': username, 'password': password})
        response = jsonify({
            '_id': str(id),
            'username': username,
            'password': password
        })
        response.status_code = 201
        return response
    else:
        return not_found()


@app.route('/users', methods=['GET'])
def get_users():
    datos = []
    users = mongo.db.users.find()
    # print(listaem)
    # response = json_util.dumps(users)
    for dat in users:
        datos.append({
            "insta_username": dat["username"],
            "insta_password": dat["password"]
        })
    print(datos)

    return jsonify(datos)


@app.route("/users/<username>")
def get_user(username):
    mongo.db.users.find_one({'username': username, })
    response = jsonify(
        {'mensaje': 'Usario nombre : ' + username + ' usuarios encontrado'})
    response.status_code = 200
    return response


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


@app.route('/users/<_id>', methods=['PUT'])
def update_user(_id):
    username = request.json['username']
    password = request.json['password']
    if username and password and _id:
        # hashed_password = generate_password_hash(password)
        mongo.db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'password': password}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
        return not_found()

# ruta de para INCLUIR TAG
# el endpoint es por metodo POST
# http://localhost:5000/tags
@app.route('/tags', methods=['POST'])
def create_tag():
    # Receiving Data
    tag = request.json['tag']

    if tag:

        id = mongo.db.tags. insert(
            {'tag': tag})
        response = jsonify({
            '_id': str(ObjectId(id)),
            'tag': tag
        })
        response.status_code = 201
        return response
    else:
        return not_found()

# ruta de para LISTA LOS TAG
# el endpoint es por metodo GET
# http://localhost:5000/tags
# tags = mongo.db.tags.find()
# ejemplicacion de este codigo
# tags es ojetos que se genera
# de objeto mongo.db que la conecion a la base datos
# mongo.db.tags donde tags es el nombre de la tabla o coleccion
# por ultimo mongo.db.tags.find() y find un metodo para buscar todos los tags de la base datos
@app.route('/tags', methods=['GET'])
def get_tags():
    datos = []
    tags = mongo.db.tags.find()
    for unTag in tags:
        datos.append({
            "id":  str(ObjectId(unTag["_id"])),
            "tag": unTag["tag"]
        })
    return jsonify(datos)

# ruta de para buscar un solo TAG
# el endpoint es por metodo GET
# http://localhost:5000/tag/<Parametro de id>
@app.route('/tag/<id>', methods=['GET'])
def get_tag(id):
    tag = mongo.db.tags.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(tag)
    clave = response("tag")
    print(clave)
    return Response(response, mimetype="application/json")


# ruta de para eliminar un solo TAG
# el endpoint es por metodo DELETE
# http://localhost:5000/tag/<Parametro de id>
@app.route('/tag/<id>', methods=['DELETE'])
def delete_tag(id):
    mongo.db.tags.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Tag-> ' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


# ruta de para actulizar un solo TAG
# el endpoint es por metodo PUT
# http://localhost:5000/tag/<Parametro de id>
@app.route('/tag/<_id>', methods=['PUT'])
def update_tag(_id):
    tag = request.json['tag']

    if tag and _id:
        # hashed_password = generate_password_hash(password)
        mongo.db.tags.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'tag': tag}})
        response = jsonify({'message': 'Tag' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True)
