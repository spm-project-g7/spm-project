from flask import Flask, request, jsonify
from sqlalchemy import and_

from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Material(db.Model):
    __tablename__ = 'learningmaterial'

    MaterialID = db.Column(db.Integer, primary_key=True)
    MaterialTitle = db.Column(db.String(255), nullable=False)
    MaterialDescription = db.Column(db.String(255), nullable=False)
    LessonID = db.Column(db.Integer, nullable=False)
    LastUpdated = db.Column(db.Date, nullable=False)
    MaterialURL = db.Column(db.String(255), nullable=False)
    MaterialType= db.Column(db.String(255), nullable=False)
    CompletedStatus = db.Column(db.String(255), nullable=False)

    def __init__(self, MaterialID, MaterialTitle, MaterialDescription, LessonID, LastUpdated, MaterialURL, MaterialType, CompletedStatus):
        self.MaterialID = MaterialID
        self.MaterialTitle = MaterialTitle
        self.MaterialDescription = MaterialDescription
        self.LessonID = LessonID
        self.LastUpdated = LastUpdated
        self.MaterialURL = MaterialURL
        self.MaterialType = MaterialType
        self.CompletedStatus = CompletedStatus
        

    def json(self):
        return {"MaterialID": self.MaterialID, "MaterialTitle": self.MaterialTitle, "LessonID": self.LessonID, "LastUpdated": self.LastUpdated,
               "MaterialURL": self.MaterialURL, "MaterialType": self.MaterialType, "CompletedStatus": self.CompletedStatus}




@app.route("/materials")
def get_all():
    materiallist = Material.query.all()
    if len(materiallist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "guess": [material.json() for material in materiallist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no materials."
        }
    ), 404


@app.route("/guess/<string:LessonID>")
def find_by_lesson(LessonID):
    materiallist = Material.query.filter_by(LessonID=LessonID).all()
    if len(materiallist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "guesses": [material.json() for material in materiallist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "materials not found."
        }
    ), 404

@app.route("/material/<string:LessonID>", methods=['POST'])
def create_material(LessonID):
    data = request.get_json()
    material = Material(LessonID, **data)

    try:
        db.session.add(material)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "user": material.json()
                },
                "message": "An error occurred uploading materials."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": material.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
