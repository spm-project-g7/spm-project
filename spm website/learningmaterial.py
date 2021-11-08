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

class LearningMaterial(db.Model):
    __tablename__ = 'learningmaterial'

    MaterialID = db.Column(db.Integer, primary_key=True)
    MaterialTitle = db.Column(db.String(255), nullable=False)
    MaterialDescription = db.Column(db.String(255), nullable=False)
    LessonID = db.Column(db.Integer, nullable=False)
    LastUpdated = db.Column(db.Date, nullable=False)
    MaterialURL = db.Column(db.String(255),nullable=True)
    MaterialType = db.Column(db.String(255),nullable=True)
    CompleteStatus = db.Column(db.String(255),nullable=True)

    def __init__(self, MaterialID, MaterialTitle, MaterialDescription, LessonID, LastUpdated, MaterialURL, MaterialType, CompleteStatus):
        self.MaterialID = MaterialID
        self.MaterialTitle = MaterialTitle
        self.MaterialDescription = MaterialDescription
        self.LessonID = LessonID
        self.LastUpdated = LastUpdated
        self.MaterialURL =  MaterialURL
        self.MaterialType = MaterialType
        self.CompleteStatus = CompleteStatus

    def json(self):
        return {"MaterialID": self.MaterialID, "MaterialTitle": self.MaterialTitle, "MaterialDescription": self.MaterialDescription, "LessonId": self.LessonID, 
                "LastUpdated": self.LastUpdated, "MaterialURL": self.MaterialURL, "MaterialType": self.MaterialType, "CompleteStatus": self.CompleteStatus}


@app.route("/learningmaterial")
def get_all():
    materiallist = LearningMaterial.query.all()
    if len(materiallist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "materials": [material.json() for material in materiallist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No material found."
        }
    ), 404

@app.route("/learningmaterial/<string:LessonID>")
def find_by_Lesson(LessonID):
    material = LearningMaterial.query.filter_by(LessonID=LessonID).first()
    if material:
        return jsonify(
            {
                "code": 200,
                "data":material.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No classes found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5008, debug=True)