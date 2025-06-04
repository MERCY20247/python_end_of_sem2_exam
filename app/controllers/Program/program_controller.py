
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Program
from app.status_codes import *

program_bp = Blueprint('program', __name__, url_prefix='/programs')

@program_bp.route('/', methods=['POST'])
def create_program():
    data = request.json
    program = Program(**data)
    db.session.add(program)
    db.session.commit()
    return jsonify({'message': 'Program created'}), HTTP_201_CREATED

@program_bp.route('/<int:id>', methods=['PUT'])
def update_program(id):
    data = request.json
    program = Program.query.get_or_404(id)
    for key, value in data.items():
        setattr(program, key, value)
    db.session.commit()
    return jsonify({'message': 'Program updated'}), HTTP_200_OK

