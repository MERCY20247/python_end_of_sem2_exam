from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for students
students = []
student_id_counter = 1

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student), 200
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students', methods=['POST'])
def add_student():
    global student_id_counter
    data = request.get_json()
    student = {
        'id': student_id_counter,
        'name': data.get('name'),
        'age': data.get('age'),
        'major': data.get('major')
    }
    students.append(student)
    student_id_counter += 1
    return jsonify(student), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    for student in students:
        if student['id'] == id:
            student['name'] = data.get('name', student['name'])
            student['age'] = data.get('age', student['age'])
            student['major'] = data.get('major', student['major'])
            return jsonify(student), 200
    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5050)
     
