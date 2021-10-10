from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from flask_sqlalchemy.utils import engine_config_warning
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Enrollment(db.Model):
    __tablename__ = 'enrollment'

    CourseID = db.Column(db.Integer, primary_key=True)
    EngineerID = db.Column(db.Integer, nullable=False)
    StartDate = db.Column(db.Date, nullable=False)
    EndDate = db.Column(db.Date, nullable=False)
    AssignedHR = db.Column(db.String(255), nullable=False)
    CourseCompleteRate = db.Column(db.Integer, nullable=False)
    CompleteStatus = db.Column(db.String(255), nullable=False)
    FinalQuizScore = db.Column(db.Integer, nullable=False)    

    def __init__(self, CourseID, EngineerID, StartDate, EndDate, AssignedHR, CourseCompleteRate, CompleteStatus, FinalQuizScore):
        self.CourseID = CourseID
        self.EngineerID = EngineerID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.AssignedHR = AssignedHR
        self.CourseCompleteRate = CourseCompleteRate
        self.CompleteStatus = CompleteStatus
        self.FinalQuizScore = FinalQuizScore

    def json(self):
        return {"CourseID": self.CourseID, "EngineerID": self.EngineerID, "StartDate": self.StartDate, "EndDate": self.EndDate, 
                "AssignedHR?": self.AssignedHR, "CourseCompleteRate": self.CourseCompleteRate, "CompleteStatus": self.CompleteStatus, 
                "FinalQuizScore": self.FinalQuizScore}


@app.route("/allenrollment")
def get_all():
    allenrollment = Enrollment.query.all()
    if len(allenrollment):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "enrollment": [enrol.json() for enrol in allenrollment]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No enrollment found."
        }
    ), 404

@app.route("/class/<string:EngineerID>")
def find_by_engineer(EngineerID):
    engineer = Enrollment.query.filter_by(EngineerID=EngineerID)
    if engineer:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "enrollment": [enrol.json() for enrol in allenrollment]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No engineer found."
        }
    ), 404

@app.route("/class/<string:CourseID>")
def find_by_course(CourseID):
    course = Enrollment.query.filter_by(CourseID=CourseID)
    if course:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "enrollment": [enrol.json() for enrol in course]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No engineer found."
        }
    ), 404


# enrol engineers into course ONLY
@app.route("/enrol/<string:CourseID>/<string:EngineerID>", methods=['POST'])
def create_enrollment(CourseID, EngineerID):
    if (Enrollment.query.filter_by(CourseID= CourseID).filter_by(EngineerID=EngineerID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "course": CourseID,
                    "engineer": EngineerID
                },
                "message": "Engineer is already enrolled in this course."
            }
        ), 400

    data = request.get_json()
    engineer = Enrollment(CourseID, EngineerID, **data)

    try:
        db.session.add(engineer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "course": CourseID,
                    "engineer": EngineerID
                },
                "message": "An error occurred enrolling the engineer."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": {
                "course": CourseID,
                "engineer": EngineerID
            },
            "message": "Successfully enrolled the engineer."
        }
    ), 201

if __name__ == '__main__':
    app.run(port=5006, debug=True)