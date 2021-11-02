from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Material(db.Model):
    __tablename__ = 'learningmaterial'

    MaterialID = db.Column(db.Integer, primary_key=True)
    MaterialTitle = db.Column(db.String(255), nullable=False)
    MaterialDescription = db.Column(db.String(255), nullable=False)
    LessonId = db.Column(db.Integer, nullable=False)
    LastUpdated = db.Column(db.Date, nullable=False)
    MaterialURL = db.Column(db.String(255), nullable=True)
    MaterialType= db.Column(db.String(255), nullable=True)
    CompleteStatus = db.Column(db.String(255), nullable=True)

    def __init__(self, MaterialID, MaterialTitle, MaterialDescription, LessonId, LastUpdated, MaterialURL, MaterialType, CompleteStatus):
        self.MaterialID = MaterialID
        self.MaterialTitle = MaterialTitle
        self.MaterialDescription = MaterialDescription
        self.LessonId = LessonId
        self.LastUpdated = LastUpdated
        self.MaterialURL = MaterialURL
        self.MaterialType = MaterialType
        self.CompleteStatus = CompleteStatus
        
    def json(self):
        return {"MaterialID": self.MaterialID, "MaterialTitle": self.MaterialTitle, "MaterialDescription": self.MaterialDescription, "LessonId": self.LessonId, 
                "LastUpdated": self.LastUpdated, "MaterialURL": self.MaterialURL, "MaterialType": self.MaterialType, "CompleteStatus": self.CompleteStatus}


@app.route("/materials")
def get_all():
    materiallist = Material.query.all()
    if len(materiallist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "material": [material.json() for material in materiallist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no materials."
        }
    ), 404


# get lessonmaterial by lessonID
@app.route("/materials/<string:LessonId>")
def find_by_lessonID(LessonId):
    materiallist = Material.query.filter_by(LessonId=LessonId)
    if materiallist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "material": [material.json() for material in materiallist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No lesson materials found."
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
    app.run(port=5007, debug=True)
