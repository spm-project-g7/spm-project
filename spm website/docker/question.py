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

class Question(db.Model):
    __tablename__ = 'question'

    QuizID = db.Column(db.Integer, primary_key=True)
    QuestionID = db.Column(db.Integer, primary_key=True, nullable=False)
    Options = db.Column(db.String, nullable=False)
    Answer = db.Column(db.String, nullable=False)
    Question = db.Column(db.String, nullable=False)

    def __init__(self, QuizID, QuestionID, Options, Answer, Question):
        self.QuizID = QuizID
        self.QuestionID = QuestionID
        self.Options = Options
        self.Answer = Answer
        self.Question = Question

    def json(self):
        return {"QuizID": self.QuizID, "QuestionID": self.QuestionID, "Options": self.Options, "Answer": self.Answer, "Question": self.Question}

# get all questions in database
@app.route("/question")
def get_all():
    questionlist = Question.query.all()
    if len(questionlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "questions": [qns.json() for qns in questionlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No questions found."
        }
    ), 404

# get question by quiz
@app.route("/question/<string:QuizID>")
def find_questions_by_quizID(QuizID):
    questionlist = Question.query.filter_by(QuizID=QuizID)
    if questionlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "questions": [qns.json() for qns in questionlist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No questions found."
        }
    ), 404

# create question
@app.route("/question/create/<string:QuestionID>", methods=['POST'])
def create_question(QuestionID):
    # if (Question.query.filter_by(QuestionID=QuizID).first()):
    #     return jsonify(
    #         {
    #             "code": 400,
    #             "data": {
    #                 "lesson": LessonID
    #             },
    #             "message": "Quiz for lesson already exists."
    #         }
    #     ), 400

    data = request.get_json()
    question = Question(QuestionID, **data)

    try:
        db.session.add(question)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "question": question.json()
                },
                "message": "An error occurred creating the quiz."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": question.json(),
            "message": "The quiz was successfully created."
        },
    ), 201


if __name__ == '__main__':
    app.run(port=5003, debug=True)