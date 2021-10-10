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

class Trainer(db.Model):
    __tablename__ = 'trainer'

    TrainerID = db.Column(db.Integer, nullable=False, primary_key=True)
    EmployeeName = db.Column(db.String(255), nullable=False)
    CurrentDesignation = db.Column(db.String(255), nullable=False)
    Department = db.Column(db.String(255), nullable=False)

    def __init__(self, TrainerID, EmployeeName, CurrentDesignation, Department):
        self.TrainerID = TrainerID
        self.EmployeeName = EmployeeName
        self.CurrentDesignation = CurrentDesignation
        self.Department = Department

    def json(self):
        return {"TrainerID": self.TrainerID, "EmployeeName": self.EmployeeName, 
                "CurrentDesignation": self.CurrentDesignation, "Department": self.Department}

@app.route("/trainer")
def get_all():
    trainerlist = Trainer.query.all()
    if len(trainerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [trainer.json() for trainer in trainerlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No trainers found."
        }
    ), 404

@app.route("/trainer/<string:TrainerID>")
def find_by_trainer(TrainerID):
    trainer = Trainer.query.filter_by(TrainerID=TrainerID).first()
    if trainer:
        return jsonify(
            {
                "code": 200,
                "data": trainer.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No trainer found."
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
    app.run(port=5000, debug=True)