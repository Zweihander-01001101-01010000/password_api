from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Josue*10',  # Cambia esto por tu contraseña
    'database': 'CartagoITech',
    'port': 3306
}

@app.route('/Amazon', methods=['GET'])
def obtener_catalogo():
    try:
        # Conexión a la base de datos MySQL
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # Obtener productos
            cursor.execute("SELECT PK_idProducto, Fk_idCategoria, Descripcion, Precio, Imagen FROM amazon")
            productos = cursor.fetchall()

            # Obtener categorías
            cursor.execute("SELECT PK_IdCategoria, Descripcion FROM categoria")
            categorias = cursor.fetchall()

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

            # Devolver los productos y categorías en formato JSON
            return jsonify({
                "productos": productos,
                "categorias": categorias
            }), 200
    except Error as e:
        # En caso de error en la base de datos, devolver un error 500
        return jsonify({"error": f"Error en la base de datos: {e}"}), 500
    except Exception as e:
        # Manejo de otros errores
        return jsonify({"error": f"Ocurrió un error: {e}"}), 500

if __name__ == '__main__':
    # Iniciar el servidor en el puerto 7000 (o el que prefieras)
    app.run(debug=True, host='0.0.0.0', port=7500)  # Cambiar puerto si es necesario