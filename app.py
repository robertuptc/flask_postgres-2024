from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
from utilities import load_data
from models import db, Students

app = Flask("server")

# Configuration for the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://@localhost:5432/students_db'
db.init_app(app)

# student data
# students = load_data("./data.csv")


@app.route("/students/", methods=['GET'])
def get_students():
    return jsonify(get_all_students())


@app.route("/old_students/", methods=['GET'])
def get_old_students():
    result = list(
        filter(lambda student: student['age'] > 19, get_all_students()))
    return jsonify(result)


@app.route("/young_students/", methods=['GET'])
def get_young_students():
    result = list(
        filter(lambda student: student['age'] < 21, get_all_students()))
    return jsonify(result)


@app.route("/advance_students/", methods=['GET'])
def get_advance_students():
    result = list(filter(
        lambda student: student['age'] < 21 and student['grade'] == 'A', get_all_students()))
    return jsonify(result)


@app.route("/student_names/", methods=['GET'])
def get_student_names():
    result = []
    for student in get_all_students():
        result.append(
            {'first_name': student['first_name'], 'last_name': student['last_name']})
    return jsonify(result)


@app.route("/student_ages/", methods=['GET'])
def get_student_ages():
    result = []
    for student in get_all_students():
        result.append(
            {"student_name": f"{student['first_name']} {student['last_name']}", 'age': student['age']})

    return jsonify(result)


def get_all_students():
    return [student.to_dictionary() for student in Students.query.all()]


app.run(debug=True, port=8000)
