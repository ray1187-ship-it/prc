"#archivo prueba de tratamiento de Datos" 
from flask import Flask, request,jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({'message': 'Bienvenido a la API de tratamiento de datos' })

@app.route('/api/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify ({'error': 'Falta datos para sumar'}), 400
    return jsonify ({'resultado': a + b})

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify ({
        'nombre': 'Microservicio Base - Tratamiento de Datos',
        'version': '1.0.0',
        'descripcion': 'esto es una prueba'
        })
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

