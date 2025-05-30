from flask import Blueprint, request, jsonify
from .db_service import get_admin, create_admin, update_password

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/register', methods=['POST'])
def register_admin():
    data = request.get_json()
    if not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email y password requeridos'}), 400
    if get_admin(data['email']):
        return jsonify({'error': 'El admin ya existe'}), 400
    create_admin(data)
    return jsonify({'message': 'Admin registrado correctamente'}), 201

@admin_bp.route('/login', methods=['POST'])
def login_admin():
    data = request.get_json()
    admin = get_admin(data.get('email'))
    if not admin or admin[1] != data.get('password'):
        return jsonify({'error': 'Credenciales inválidas'}), 401
    return jsonify({'email': admin[0], 'name': admin[2]}), 200

@admin_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('new_password')
    if not get_admin(email):
        return jsonify({'error': 'Admin no encontrado'}), 404
    update_password(email, new_password)
    return jsonify({'message': 'Contraseña actualizada correctamente'}), 200 