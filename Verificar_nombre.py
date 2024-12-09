from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost',       # Cambia según tu configuración
    'user': 'root',            # Cambia según tu configuración
    'password': 'Josue*10',    # Cambia según tu configuración
    'database': 'CartagoITech', # Cambia según tu base de datos
    'port': 3306               # Cambia según tu configuración
}

# Crear la aplicación Flask
app = Flask(__name__)

# API para verificar si el nombre está registrado en la tabla TSE
@app.route('/verificar_nombre', methods=['GET'])
def verificar_nombre():
    nombre = request.args.get('nombre')  # Obtener el nombre desde los parámetros GET
    if not nombre:
        return jsonify({"success": False, "message": "El nombre es requerido"}), 400

    try:
        # Establecer conexión con la base de datos MySQL
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta para verificar si el nombre existe en la tabla TSE
            cursor.execute("SELECT COUNT(*) FROM TSE WHERE Nombre = %s", (nombre,))
            count = cursor.fetchone()[0]

            cursor.close()
            connection.close()

            if count > 0:
                return jsonify({"success": False, "message": "El nombre ya está registrado."}), 200
            else:
                return jsonify({"success": True, "message": "El nombre está disponible."}), 200

    except Error as e:
        return jsonify({"success": False, "message": f"Error en la base de datos: {e}"}), 500

    except Exception as e:
        return jsonify({"success": False, "message": f"Ocurrió un error: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)  # API en el puerto 9000
