from flask import Flask
from app.extensions import db,migrate
from app.models import db
from app.controllers.blueprint import student_bp, course_bp, program_bp 
from flask_migrate import Migrate



#application factory function
def create_app():
    
    #app instance
    app = Flask(__name__)
    # Database URI and configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/python_exam_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True  # Enable debug mode

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints with their respective prefixes
    app.register_blueprint(student_bp, url_prefix='/students')  
    app.register_blueprint(course_bp, url_prefix='/courses')     
    app.register_blueprint(program_bp, url_prefix='/programs')  

    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app,db)


    @app.route("/")
    def exam_page():
     return """
    <html>
    <head>
        <title>Exam Landing Page</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #e0c3fc, #8ec5fc);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #6a0dad;
                font-size: 2em;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.1em;
                color: #333;
            }
            .btn {
                margin-top: 20px;
                padding: 12px 24px;
                font-size: 1em;
                background-color: #6a0dad;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                text-decoration: none;
            }
            .btn:hover {
                background-color: #530baf;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Welcome to the Intermediate Python Exam</h1>
            <p>Congratulations, you have successfully launched the app!</p>
            <p>You may now embark on the exam. Stay focused and give it your best shot.</p>
            <a href="#" class="btn">Good Luck 💪🚀</a>
        </div>
    </body>
    </html>
    """


 
    
  
    
    

    return app

