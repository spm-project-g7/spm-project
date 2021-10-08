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

class Quiz(db.Model):
    __tablename__ = 'quiz'

    QuizID = db.Column(db.Integer, nullable=False)
    LastUpdated = db.Column(db.Date, nullable=False)
    GradedQuiz = db.Column(db.SmallInteger, nullable=False)
    PassingGrade = db.Column(db.Intger, nullable=False)
    LessonID = db.Column(db.Integer, nullable=False)
    QuizScore = db.Column(db.Integer, nullable=False)
    CompleteStatus = db.Column(db.String(255), nullable=False)

    def __init__(self, QuizID, LastUpdated, GradedQuiz, PassingGrade, LessonID, QuizScore, CompleteStatus):
        self.QuizID = QuizID
        self.LastUpdated = LastUpdated
        self.GradedQuiz = GradedQuiz
        self.PassingGrade = PassingGrade
        self.LessonID = LessonID
        self.QuizScore = QuizScore
        self.CompleteStatus = CompleteStatus

    def json(self):
        return {"QuizID": self.QuizID, "LastUpdated": self.LastUpdated, "GradedQuiz": self.GradedQuiz, 
                "PassingGrade": self.PassingGrade, "LessonID": self.LessonID, "QuizScore": self.QuizScore,
                "CompleteStatus": self.CompleteStatus}

# get all quizzes in database
@app.route("/allquizzes")
def get_all():
    quizlist = Quiz.query.all()
    if len(quizlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [quiz.json() for quiz in quizlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No quiz found."
        }
    ), 404

# get quiz by lesson
@app.route("/quiz/<string:lessonID>")
def find_by_trainer(LessonID):
    quiz = Quiz.query.filter_by(LessonID=LessonID).first()
    if quiz:
        return jsonify(
            {
                "code": 200,
                "data": quiz.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No quiz found."
        }
    ), 404

# get questions by quiz
@app.route("/quiz/<string:lessonID>")
def find_by_trainer(LessonID):
    quiz = Quiz.query.filter_by(LessonID=LessonID).first()
    if quiz:
        return jsonify(
            {
                "code": 200,
                "data": quiz.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No quiz found."
        }
    ), 404

# create quiz
@app.route("/quiz/<string:lessonID>", methods=['POST'])
def create_class(LessonID):
    if (Quiz.query.filter_by(LessonID=LessonID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "lesson": LessonID
                },
                "message": "Quiz for lesson already exists."
            }
        ), 400

    data = request.get_json()
    quiz = Quiz(LessonID, **data)

    try:
        db.session.add(quiz)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "quiz": quiz.json()
                },
                "message": "An error occurred creating the quiz."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": quiz.json(),
            "message": "The quiz was successfully created."
        },
    ), 201

if __name__ == '__main__':
    app.run(port=5003, debug=True)