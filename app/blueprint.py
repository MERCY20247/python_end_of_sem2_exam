from flask import Blueprint

# Define the blueprints only once
student_bp = Blueprint('student', __name__, url_prefix='/students')
course_bp = Blueprint('course', __name__, url_prefix='/courses')
program_bp = Blueprint('program', __name__, url_prefix='/programs')

# Import the controller files which should define routes
from .student.controller import *
from .course.controller import *
from .program.controller import *
