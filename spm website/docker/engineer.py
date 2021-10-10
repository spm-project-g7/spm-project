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

class Engineer(db.Model):
    __tablename__ = 'engineer'

    EngineerID = db.Column(db.Integer, primary_key=True)
    EmployeeName = db.Column(db.String(255), nullable=False)
    CurrentDesignation = db.Column(db.String(255), nullable=False)
    Department = db.Column(db.String(255), nullable=False)

    def __init__(self, EngineerID, EmployeeName, CurrentDesignation, Department):
        self.EngineerID = EngineerID
        self.EmployeeName = EmployeeName
        self.CurrentDesignation = CurrentDesignation
        self.Department = Department

    def json(self):
        return {"EngineerID": self.EngineerID, "EmployeeName": self.EmployeeName, "CurrentDesignation": self.CurrentDesignation, "Department": self.Department}

@app.route("/engineer")
def get_all():
    engineerlist = Engineer.query.all()
    if len(engineerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "engineers": [engineer.json() for engineer in engineerlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No engineers found."
        }
    ), 404

@app.route("/learner/<string:EngineerID>")
def find_by_learner(EngineerID):
    engineer = Engineer.query.filter_by(EngineerID=EngineerID).first()
    if engineer:
        return jsonify(
            {
                "code": 200,
                "data": engineer.json()
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
    app.run(port=5002, debug=True)