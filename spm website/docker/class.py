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
    ClasSize = db.Column(db.Integer, nullable=False)    

    def __init__(self, ClassID, TrainerID, CourseID, StartDate, EndDate, StartTime, ClasSize):
        self.ClassID = ClassID
        self.TrainerID = TrainerID
        self.CourseID = CourseID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.ClasSize = ClasSize

    def json(self):
        return {"ClassID": self.ClassID, "TrainerID": self.TrainerID, "CourseID": self.CourseID, 
                "StartDate": self.StartDate, "EndDate": self.EndDate, "ClasSize": self.ClasSize}


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

@app.route("/class/<string:trainer>")
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

# dk abt this part need edit
@app.route("/user/<string:classname>", methods=['POST'])
def create_class(classname):
    if (Classes.query.filter_by(ClassID=ClassID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "email": email
                },
                "message": "Email already exists."
            }
        ), 400

    data = request.get_json()
    user = User(email, **data)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "user": user.json()
                },
                "message": "An error occurred creating the user."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(port=5004, debug=True)