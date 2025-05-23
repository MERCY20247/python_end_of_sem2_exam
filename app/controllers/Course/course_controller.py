from flask import request, jsonify, Blueprint
from app.models import db, Course, Student

course_bp = Blueprint('course', __name__)

# Create a new course
@course_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    title = data.get('title')
    lecturer = data.get('lecturer')
    student_id = data.get('student_id')

    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found."}), 404
    
    new_course = Course(title=title, lecturer=lecturer, student_id=student_id)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully"}), 200

