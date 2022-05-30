import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
lista_productos = [
    {
        'nombre': 'camiseta',
        'cantidad': 45
    },
    {
        'nombre': 'calcetines',
        'cantidad': 75
    },
    {
        'nombre': 'tenis',
        'cantidad': 12
    }
]


@cross_origin
@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        print(request.json)
        return jsonify({
            'mensaje': 'Hola desde el metodo POST'
        })
    
    return jsonify({
        'mensaje': 'Listado de productos',
        'data': lista_productos
    })


if __name__ == '__main__':
    app.run()