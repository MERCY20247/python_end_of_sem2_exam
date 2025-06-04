
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Student, Program
from app.status_codes import *

student_bp = Blueprint('student', __name__, url_prefix='/students')

#create a student
@student_bp.route('/', methods=['POST'])
def create_student():
    data = request.json

    #validate presence of required fields
    required_fields = ['name', 'course', 'email', 'date_of_birth', 'program_id']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), HTTP_400_BAD_REQUEST

    #validate program_id exists
    program = Program.query.get(data['program_id'])
    if not program:
        return jsonify({'error': 'Invalid program_id'}), HTTP_400_BAD_REQUEST

    #create student
    student = Student(
        name=data['name'],
        course=data['course'],
        email=data['email'],
        date_of_birth=data['date_of_birth'],
        program_id=data['program_id']
    )
    db.session.add(student)
    db.session.commit()

    return jsonify({'message': 'Student created', 'student_id': student.id}), HTTP_201_CREATED

#get all students
@student_bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    results = []
    for student in students:
        results.append({
            'id': student.id,
            'name': student.name,
            'course': student.course,
            'email': student.email,
            'date_of_birth': student.date_of_birth.isoformat(),
            'program_id': student.program_id
        })
    return jsonify(results), HTTP_200_OK

#delete a student
@student_bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), HTTP_404_NOT_FOUND

    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'}), HTTP_200_OK
