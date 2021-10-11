from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Classes(db.Model):
    __tablename__ = 'class'

    ClassID = db.Column(db.Integer, primary_key=True)
    TrainerID = db.Column(db.Integer, nullable=False)
    CourseID = db.Column(db.Integer, nullable=False)
    StartDate = db.Column(db.Date, nullable=False)
    EndDate = db.Column(db.Date, nullable=False)
    StartTime = db.Column(db.String(255), nullable=False)
    EndTime = db.Column(db.String(255), nullable=False)
    ClassName = db.Column(db.String(255), nullable=False)
    ClassSize = db.Column(db.Integer, nullable=False)   

    def __init__(self, ClassID, TrainerID, CourseID, StartDate, EndDate, StartTime, EndTime, ClassName, ClassSize):
        self.ClassID = ClassID
        self.TrainerID = TrainerID
        self.CourseID = CourseID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.ClassName = ClassName
        self.ClassSize = ClassSize

    def json(self):
        return {"ClassID": self.ClassID, "TrainerID": self.TrainerID, "CourseID": self.CourseID, "StartDate": self.StartDate, 
                "EndDate": self.EndDate, "StartTime": self.StartTime, "EndTime": self.EndTime, "ClassName": self.ClassName, 
                "ClassSize": self.ClassSize}


@app.route("/class")
def get_all():
    classlist = Classes.query.all()
    if len(classlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [classname.json() for classname in classlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No classes found."
        }
    ), 404

@app.route("/class/<string:TrainerID>")
def find_by_trainer(TrainerID):
    classlist = Classes.query.filter_by(TrainerID=TrainerID)
    if classlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [classname.json() for classname in classlist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No classes found."
        }
    ), 404

if __name__ == '__main__':
    app.run(port=5005, debug=True)