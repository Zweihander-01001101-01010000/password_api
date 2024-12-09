from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)  # Habilitar CORS

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Josue*10',
    'database': 'CartagoITech',
    'port': 3306
}

@app.route('/proveedores', methods=['GET'])
def obtener_proveedores():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = "SELECT Nombre, TipoDeProductos FROM Proveedores"
            cursor.execute(query)
            proveedores = cursor.fetchall()
            return jsonify(proveedores), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(port=9500, debug=True)
