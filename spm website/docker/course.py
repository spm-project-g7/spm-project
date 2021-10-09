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

class Course(db.Model):
    __tablename__ = 'course'

    CourseID = db.Column(db.Integer, primary_key=True)
    CourseName = db.Column(db.String(255), nullable=False)
    CourseValidStartDate = db.Column(db.Date, nullable=False)
    CourseValidEndDate = db.Column(db.Date, nullable=False)
    CreatedBy = db.Column(db.Integer, nullable=False)

    def __init__(self, CourseID, CourseName, CourseValidStartDate, CourseValidEndDate, CreatedBy):
        self.CourseID = CourseID
        self.CourseName = CourseName
        self.CourseValidStartDate = CourseValidStartDate
        self.CourseValidEndDate = CourseValidEndDate
        self.CreatedBy = CreatedBy

    def json(self):
        return {"CourseID": self.CourseID, "CourseName": self.CourseName, "CourseValidStartDate": self.CourseValidStartDate, 
                "CourseValidEndDate": self.CourseValidEndDate, "CreatedBy": self.CreatedBy}


@app.route("/course")
def get_all():
    courselist = Course.query.all()
    if len(courselist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": [course.json() for course in courselist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No courses found."
        }
    ), 404

@app.route("/course/<string:CourseID>")
def find_by_course(CourseID):
    course = Course.query.filter_by(CourseID=CourseID).first()
    if course:
        return jsonify(
            {
                "code": 200,
                "data": course.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No course found."
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