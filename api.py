from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://cmongo.dbmongo.svc.cluster.local:27017/')
db = client['mydatabase']
collection = db['people']

@app.route('/')
def listar_personas():
    print('Listando personas...')
    personas = list(collection.find({}, {'_id': 0}))
    return jsonify(personas)

@app.route('/crear', methods=['POST'])
def crear_persona():
    print('Creando persona...')
    data = request.get_json()
    nombre = data.get('nombre')
    fecha_cumple = data.get('fecha_cumple')

    persona = {'nombre': nombre, 'fecha_cumple': fecha_cumple}
    collection.insert_one(persona)
    return 'Persona creada exitosamente', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
