from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
db_config = {
     'host': 'localhost',         # Dirección del servidor MySQL
    'user': 'root',              # Usuario de MySQL
    'password': 'Josue*10', # Cambia esto por tu contraseña
    'database': 'CartagoITech',           # Base de datos
    'port': 3306  
}

# Ruta para crear la cita
@app.route('/crear_cita', methods=['POST'])
def crear_cita():
    try:
        # Obtener los datos desde el cuerpo de la solicitud
        data = request.get_json()
        correo_usuario = data.get('correoUsuario')
        motivo = data.get('motivo')

        if not correo_usuario or not motivo:
            return jsonify({"error": "Faltan datos necesarios (correoUsuario y motivo)"}), 400

        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()
            query = "INSERT INTO cita (FK_Correo, Motivo) VALUES (%s, %s)"
            cursor.execute(query, (correo_usuario, motivo))

            # Confirmar la transacción
            connection.commit()

            cursor.close()
            connection.close()

            # Responder con un mensaje de éxito
            return jsonify({"message": "Cita registrada exitosamente"}), 200

    except Error as e:
        # En caso de error en la base de datos
        return jsonify({"error": f"Error en la base de datos: {e}"}), 500
    except Exception as e:
        # En caso de cualquier otro error
        return jsonify({"error": f"Ocurrió un error: {e}"}), 500

if __name__ == '__main__':
    # Cambiar puerto e IP a lo que se desee
    app.run(debug=True, host='0.0.0.0', port=6000)  
