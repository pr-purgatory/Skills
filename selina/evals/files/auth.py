import os
import jwt
import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

SECRET = os.environ.get('JWT_SECRET', 'dev-secret-key')
DB_PATH = os.environ.get('DB_PATH', './users.db')

def get_db():
    return sqlite3.connect(DB_PATH)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    db = get_db()
    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        token = jwt.encode({
            'user_id': user[0],
            'exp': datetime.utcnow() + timedelta(days=365)
        }, SECRET, algorithm='HS256')
        return jsonify({'token': token})

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/admin', methods=['GET'])
def admin():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token'}), 401

    try:
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        user_id = payload['user_id']

        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        user = cursor.fetchone()

        if user[4] == 'admin':
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return jsonify({'users': users})
    except Exception as e:
        return jsonify({'error': str(e)}), 401

    return jsonify({'error': 'Forbidden'}), 403

@app.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    email = data['email']
    db = get_db()
    cursor = db.cursor()
    cursor.execute(f"SELECT id FROM users WHERE email = '{email}'")
    user = cursor.fetchone()
    if user:
        new_password = email.split('@')[0] + '123'
        cursor.execute(f"UPDATE users SET password = '{new_password}' WHERE id = {user[0]}")
        db.commit()
        return jsonify({'message': f'Password reset to {new_password}'})
    return jsonify({'error': 'Email not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
