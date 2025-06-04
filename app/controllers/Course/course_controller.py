
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Course
from app.status_codes import *

course_bp = Blueprint('course', __name__, url_prefix='/courses')

@course_bp.route('/', methods=['POST'])
def create_course():
    data = request.json
    course = Course(**data)
    db.session.add(course)
    db.session.commit()
    return jsonify({'message': 'Course created'}), HTTP_201_CREATED

