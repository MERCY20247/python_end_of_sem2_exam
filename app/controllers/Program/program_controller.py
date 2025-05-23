from flask import request, jsonify, Blueprint
from app.models import db, Program

program_bp = Blueprint('program', __name__)

# Create a new program
@program_bp.route('/', methods=['POST'])
def create_program():
    data = request.get_json()
    name = data.get('name')
    director = data.get('director')

    if not name or not director:
        return jsonify({"message": "Missing required fields (name, address)"}), 400

    new_program = Program(name=name, director=director)
    db.session.add(new_program)
    db.session.commit()

    return jsonify({"message": "Program created successfully!"}), 201


# Update a program
@program_bp.route('/<int:id>', methods=['PUT'])
def update_program(id):
    data = request.get_json()
    program = Program.query.get(id)
    if not program:
        return jsonify({"message": "Program not found."}), 404
    
    program.name = data.get('name', program.name)
    program.director = data.get('director', program.address)
    db.session.commit()

    return jsonify({"message": "Company updated successfully!"}), 200

