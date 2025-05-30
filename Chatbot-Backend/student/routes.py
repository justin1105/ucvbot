from flask import Blueprint, request, jsonify
from .db_service import get_student, create_student, update_student

student_bp = Blueprint('student', __name__)

@student_bp.route('/<uid>', methods=['GET'])  # Nueva ruta para el endpoint que fallaba
def get_student_by_uid(uid):
    uid = uid.strip()  # Limpieza de espacios
    student = get_student(uid)
    if not student:
        return jsonify({'error': 'Estudiante no encontrado'}), 404
    
    # Estructura de respuesta estandarizada
    response = {
        'userUID': student[0],
        'userName': student[1],
        'email': student[2],
        'photoURL': student[3],
        'level': {'id': student[4]},
        'correctExercises': student[5],
        'incorrectExercises': student[6],
        'score': student[7]
    }
    return jsonify(response), 200

@student_bp.route('/login', methods=['POST'])
def login_student():
    data = request.get_json()
    userUID = data.get('userUID', '').strip()  # Limpieza del UID
    
    if not userUID:
        return jsonify({'error': 'userUID requerido'}), 400

    # Validación de correo institucional (opcional)
    email = data.get('email', '')
    if email and not email.endswith('@ucv.edu.pe'):
        return jsonify({'error': 'Solo correos institucionales @ucv.edu.pe'}), 403

    # Lógica de estudiante existente/nuevo
    student = get_student(userUID)
    if not student:
        create_student(data)
        student = get_student(userUID)

    # Respuesta estructurada (consistente con GET)
    student_dict = {
        'userUID': student[0],
        'userName': student[1],
        'email': student[2],
        'photoURL': student[3],
        'level': {'id': student[4]},
        'correctExercises': student[5],
        'incorrectExercises': student[6],
        'score': student[7]
    }
    return jsonify(student_dict), 200