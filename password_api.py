from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt

app = Flask(__name__)
CORS(app)  # Permite solicitudes de diferentes orígenes (CORS)

@app.route('/hash_password', methods=['POST'])
def hash_password():
    try:
        data = request.json
        if 'password' not in data:
            return jsonify({'error': 'Password is required'}), 400
        
        password = data['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return jsonify({'hashed_password': hashed.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/verify_password', methods=['POST'])
def verify_password():
    try:
        data = request.json
        if 'password' not in data or 'hashed_password' not in data:
            return jsonify({'error': 'Password and hashed_password are required'}), 400
        
        password = data['password'].encode('utf-8')
        hashed_password = data['hashed_password'].encode('utf-8')
        is_valid = bcrypt.checkpw(password, hashed_password)
        return jsonify({'is_valid': is_valid}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
