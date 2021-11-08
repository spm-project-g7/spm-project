from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from os import environ, linesep
from flask_cors import CORS
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Lesson(db.Model):
    __tablename__ = 'lesson'

    LessonID = db.Column(db.Integer, nullable=False, primary_key=True)
    TrainerID = db.Column(db.Integer, nullable=False)
    ClassID = db.Column(db.Integer, nullable=False)
    PrerequisiteLessonID = db.Column(db.Integer, nullable=True)
    LessonName = db.Column(db.String(255), nullable=False)

    def __init__(self, LessonID, TrainerID, Department, ClassID, PrerequisiteLessonID,LessonName):
        self.LessonID = LessonID
        self.TrainerID = TrainerID
        self.Department = Department
        self.ClassID = ClassID
        self.PrerequisiteLessonID = PrerequisiteLessonID
        self.LessonName = LessonName

    def json(self):
        return {"LessonID": self.LessonID,"TrainerID": self.TrainerID, "ClassID": self.ClassID, "PrerequisiteLessonID": self.PrerequisiteLessonID, "LessonName": self.LessonName}

# get all lessons in database
@app.route("/lesson")
def get_all():
    lessonlist = Lesson.query.all()
    if len(lessonlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lessons": [lesson.json() for lesson in lessonlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No lesson found."
        }
    ), 404

# get lesson by class
@app.route("/class/<string:ClassID>")
def find_by_class(ClassID):
    lesson = Lesson.query.filter_by(ClassID=ClassID).first()
    if lesson:
        return jsonify(
            {
                "code": 200,
                "data": lesson.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No lesson found."
        }
    ), 404

# create lesson
@app.route("/lesson/<string:lessonID>", methods=['POST'])
def create_class(LessonID):
    if (Lesson.query.filter_by(LessonID=LessonID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "lesson": LessonID
                },
                "message": "Lesson for class already exists."
            }
        ), 400

    data = request.get_json()
    lesson = Lesson(LessonID, **data)

    try:
        db.session.add(lesson)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "quiz": lesson.json()
                },
                "message": "An error occurred creating the lesson."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": lesson.json(),
            "message": "The lesson was successfully created."
        },
    ), 201

# get lesson list by class
@app.route("/lessonlist/<string:ClassID>")
def find_lessonlist_by_class(ClassID):
    lessonList = Lesson.query.filter_by(ClassID=ClassID)
    if lessonList:
        return jsonify(
            {
                "code": 200,
                "data": {
                   "lessonList": [lesson.json() for lesson in lessonList]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No lessons found."
        }
    ), 404

    # get lesson list by class
@app.route("/singlelesson/<string:LessonID>")
def find_singlelesson_by_class(LessonID):
    lessonobj = Lesson.query.filter_by(LessonID=LessonID).first()
    if lessonobj:
        return jsonify(
            {
                "code": 200,
                "data": lessonobj.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No lessons found."
        }
    ), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)