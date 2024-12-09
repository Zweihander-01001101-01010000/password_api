from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/comprar', methods=['POST'])
def comprar():
    data = request.json

    tarjeta = data.get('tarjeta')
    codigo_seguridad = data.get('codigo_seguridad')
    total_compra = data.get('total_compra')

    # Aquí debes validar la tarjeta y el código de seguridad (lógica de negocio)
    if not tarjeta or not codigo_seguridad:
        return jsonify({'estado': 'error', 'mensaje': 'Datos incompletos. Faltan tarjeta o código de seguridad.'}), 400
    
    # Lógica de validación
    if len(tarjeta) != 16:  # Ejemplo de validación de tarjeta
        return jsonify({'estado': 'error', 'mensaje': 'Número de tarjeta inválido.'}), 400
    
    if len(codigo_seguridad) != 3:  # Ejemplo de validación de código de seguridad
        return jsonify({'estado': 'error', 'mensaje': 'Código de seguridad inválido.'}), 400
    
    # Lógica de pago (simulada)
    if tarjeta == '4111111111111111' and codigo_seguridad == '123':  # Tarjeta de prueba
        return jsonify({'estado': 'exitoso', 'mensaje': 'Compra realizada con éxito.'}), 200
    else:
        return jsonify({'estado': 'error', 'mensaje': 'Error al procesar el pago.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=10500)
