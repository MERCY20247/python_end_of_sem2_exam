
from flask import Blueprint
from app.Controllers.Course.course_controller import course_bp
from app.Controllers.Student.student_controller import student_bp
from app.Controllers.Program.program_controller import program_bp

# These are the blueprints
__all__ = ['course_bp', 'student_bp', 'program_bp']
