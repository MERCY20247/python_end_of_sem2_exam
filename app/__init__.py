from flask import Flask
from config import Config
from app.extensions import db, migrate
from app.models import Program, Course, Student 
from app.blueprint import course_bp, student_bp, program_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(course_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(program_bp)

    #create tables 
    with app.app_context():
        db.create_all()

    return app
