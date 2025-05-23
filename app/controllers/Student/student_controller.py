from flask import request, jsonify, Blueprint
from app.models import db, Student

student_bp = Blueprint('student', __name__, url_prefix='/students')

# Create a new student
@student_bp.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    course = data.get('course')

    if not name or not course:
        return jsonify({"message": "Missing required fields (name, course)"}), 400

    new_student = Student(name=name, course=course)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student created successfully!"}), 201

# Get all students
@student_bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    # Returning structured response 
    return jsonify([{"id": student.id, "name": student.name, "email": student.email,"date_of_birth": student.date_of_birth, "course" :student.course} for student in students]), 200

# Delete a student
@student_bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"message": "Student not found."}), 404
    
    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully!"}), 200


