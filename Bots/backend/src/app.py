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

    if username and  password:
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

    # return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    print(id)

    user = mongo.db.story_by_users.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    clave = response("password")
    print(clave)
    return Response(response, mimetype="application/json")


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
    if username and  password and _id:
        # hashed_password = generate_password_hash(password)
        mongo.db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'password': password}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
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
