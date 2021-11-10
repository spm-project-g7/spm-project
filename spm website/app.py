from flask import Flask, request, jsonify, render_template

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


# @app.route('/')
# def home():
#    return render_template('Homepage.html')

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
    ClassDay = db.Column(db.String(255), nullable=False)

    def __init__(self, ClassID, TrainerID, CourseID, StartDate, EndDate, StartTime, EndTime, ClassName, ClassSize, ClassDay):
        self.ClassID = ClassID
        self.TrainerID = TrainerID
        self.CourseID = CourseID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.ClassName = ClassName
        self.ClassSize = ClassSize
        self.ClassDay = ClassDay

    def json(self):
        return {"ClassID": self.ClassID, "TrainerID": self.TrainerID, "CourseID": self.CourseID, "StartDate": self.StartDate,
                "EndDate": self.EndDate, "StartTime": self.StartTime, "EndTime": self.EndTime, "ClassName": self.ClassName,
                "ClassSize": self.ClassSize, "ClassDay": self.ClassDay}


@app.route("/class")
def get_all_classes():
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


@app.route("/class/trainer/<string:TrainerID>")
def find_class_by_trainer(TrainerID):
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


@app.route("/class/course/<string:CourseID>")
def find_by_CourseID(CourseID):
    classlist = Classes.query.filter_by(CourseID=CourseID)
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

# get single class by course ID


@app.route("/class/singleclass/<string:CourseID>")
def find_singleclass_by_CourseID(CourseID):
    classObj = Classes.query.filter_by(CourseID=CourseID).first()
    if classObj:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classobj": classObj.json()
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No class found."
        }
    ), 404


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
def get_all_courses():
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
def find_by_courseID(CourseID):
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
def get_all_engineers():
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
            "message": "No engineer found."
        }
    ), 404


@app.route("/engineer/<string:EngineerID>")
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
            "message": "No engineer found."
        }
    ), 404


class Enrollment(db.Model):
    __tablename__ = 'enrollment'

    CourseID = db.Column(db.Integer, primary_key=True)
    ClassID = db.Column(db.Integer, nullable=False)
    EngineerID = db.Column(db.Integer, nullable=False)
    StartDate = db.Column(db.Date, nullable=False)
    EndDate = db.Column(db.Date, nullable=False)
    AssignedHR = db.Column(db.String(255), nullable=False)
    CourseCompleteRate = db.Column(db.Integer, nullable=False)
    CompleteStatus = db.Column(db.String(255), nullable=False)
    FinalQuizScore = db.Column(db.Integer, nullable=False)

    def __init__(self, CourseID, ClassID, EngineerID, StartDate, EndDate, AssignedHR, CourseCompleteRate, CompleteStatus, FinalQuizScore):
        self.CourseID = CourseID
        self.ClassID = ClassID
        self.EngineerID = EngineerID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.AssignedHR = AssignedHR
        self.CourseCompleteRate = CourseCompleteRate
        self.CompleteStatus = CompleteStatus
        self.FinalQuizScore = FinalQuizScore

    def json(self):
        return {"CourseID": self.CourseID, "ClassID": self.ClassID, "EngineerID": self.EngineerID, "StartDate": self.StartDate, "EndDate": self.EndDate,
                "AssignedHR": self.AssignedHR, "CourseCompleteRate": self.CourseCompleteRate, "CompleteStatus": self.CompleteStatus,
                "FinalQuizScore": self.FinalQuizScore}


@app.route("/allenrollment")
def get_all_enrollment():
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


# @app.route("/class/<string:EngineerID>")
# def find_by_engineer(EngineerID):
#     engineer = Enrollment.query.filter_by(EngineerID=EngineerID)
#     if engineer:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "enrollment": [enrol.json() for enrol in engineer]
#                 }
#             }
#         ), 200
#     return jsonify(
#         {
#             "code": 404,
#             "message": "No engineer found."
#         }
#     ), 404


# @app.route("/class/<string:CourseID>")
# def find_by_course(CourseID):
#     course = Enrollment.query.filter_by(CourseID=CourseID).all()
#     if len(course):
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "enrollment": [enrol.json() for enrol in course]
#                 }
#             }
#         ), 200
#     return jsonify(
#         {
#             "code": 404,
#             "message": "No engineer found."
#         }
#     ), 404


# enrol engineers into course and class
@app.route("/enrol/<string:CourseID>/<string:EngineerID>/<string:ClassID>", methods=['POST'])
def create_enrollment(CourseID, EngineerID, ClassID):
    if (Enrollment.query.filter_by(CourseID=CourseID).filter_by(EngineerID=EngineerID).filter_by(ClassID=ClassID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "course": CourseID,
                    "engineer": EngineerID,
                    "class": ClassID
                },
                "message": "Engineer is already enrolled in this course and class."
            }
        ), 400

    data = request.get_json()
    engineer = Enrollment(CourseID, EngineerID, ClassID, **data)

    try:
        db.session.add(engineer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "course": CourseID,
                    "engineer": EngineerID,
                    "class": ClassID
                },
                "message": "An error occurred enrolling the engineer."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": {
                "course": CourseID,
                "engineer": EngineerID,
                "class": ClassID
            },
            "message": "Successfully enrolled the engineer."
        }
    ), 201

#self enrol engineers into course and class
@app.route("/enrolself/<string:CourseID>/<string:EngineerID>/<string:ClassID>", methods=['POST'])
def create_self_enrollment(CourseID, EngineerID, ClassID):
    if (Enrollment.query.filter_by(CourseID=CourseID).filter_by(EngineerID=EngineerID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "course": CourseID,
                    "engineer": EngineerID,
                    "class": ClassID
                },
                "message": "Engineer is already enrolled in this course and class."
            }
        ), 400

    data = request.get_json()
    engineer = Enrollment(ClassID, CourseID, EngineerID, **data)

    try:
        db.session.add(engineer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "course": CourseID,
                    "engineer": EngineerID,
                    "class": ClassID
                },
                "message": "An error occurred enrolling the engineer."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": {
                "course": CourseID,
                "engineer": EngineerID,
                "class": ClassID
            },
            "message": "Successfully enrolled the engineer."
        }
    ), 201

# get enrollment by engineerId


@app.route("/enrollment/<string:EngineerID>")
def find_enrollment_by_engineer(EngineerID):
    enrollment = Enrollment.query.filter_by(EngineerID=EngineerID).first()
    if enrollment:
        return jsonify(
            {
                "code": 200,
                "data": enrollment.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No enrollment found."
        }
    ), 404


class Lesson(db.Model):
    __tablename__ = 'lesson'

    LessonID = db.Column(db.Integer, nullable=False, primary_key=True)
    TrainerID = db.Column(db.Integer, nullable=False)
    ClassID = db.Column(db.Integer, nullable=False)
    PrerequisiteLessonID = db.Column(db.Integer, nullable=True)
    LessonName = db.Column(db.String(255), nullable=False)

    def __init__(self, LessonID, TrainerID, ClassID, PrerequisiteLessonID, LessonName):
        self.LessonID = LessonID
        self.TrainerID = TrainerID
        self.ClassID = ClassID
        self.PrerequisiteLessonID = PrerequisiteLessonID
        self.LessonName = LessonName

    def json(self):
        return {"LessonID": self.LessonID, "TrainerID": self.TrainerID, "ClassID": self.ClassID, "PrerequisiteLessonID": self.PrerequisiteLessonID, "LessonName": self.LessonName}

# get all lessons in database


@app.route("/lesson")
def get_all_lessons():
    lessonlist = Lesson.query.all()
    if len(lessonlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lessons": [lesson.json() for lesson in lessonlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No lesson found."
        }
    ), 404

# get lesson by class


@app.route("/class/<string:ClassID>")
def find_by_class(ClassID):
    lesson = Lesson.query.filter_by(ClassID=ClassID).first()
    if lesson:
        return jsonify(
            {
                "code": 200,
                "data": lesson.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No lesson found."
        }
    ), 404

# create lesson


@app.route("/lesson/<string:LessonID>", methods=['POST'])
def create_class(LessonID):
    if (Lesson.query.filter_by(LessonID=LessonID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "lesson": LessonID
                },
                "message": "Lesson for class already exists."
            }
        ), 400

    data = request.get_json()
    lesson = Lesson(LessonID, **data)

    try:
        db.session.add(lesson)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "quiz": lesson.json()
                },
                "message": "An error occurred creating the lesson."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": lesson.json(),
            "message": "The lesson was successfully created."
        },
    ), 201

# get lesson list by class


@app.route("/lessonlist/<string:ClassID>")
def find_lessonlist_by_class(ClassID):
    lessonList = Lesson.query.filter_by(ClassID=ClassID)
    if lessonList:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lessonList": [lesson.json() for lesson in lessonList]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No lessons found."
        }
    ), 404


class Quiz(db.Model):
    __tablename__ = 'quiz'

    QuizID = db.Column(db.Integer, primary_key=True)
    LastUpdated = db.Column(db.Date, nullable=False)
    GradedQuiz = db.Column(db.SmallInteger, nullable=False)
    PassingGrade = db.Column(db.Integer, nullable=False)
    LessonID = db.Column(db.Integer, nullable=False)
    QuizScore = db.Column(db.Integer, nullable=True)
    QuizName = db.Column(db.String(255), nullable=True)
    QuizTime = db.Column(db.Integer, nullable=True)

    def __init__(self, QuizID, LastUpdated, GradedQuiz, PassingGrade, LessonID, QuizScore, QuizName, QuizTime):
        self.QuizID = QuizID
        self.LastUpdated = LastUpdated
        self.GradedQuiz = GradedQuiz
        self.PassingGrade = PassingGrade
        self.LessonID = LessonID
        self.QuizScore = QuizScore
        self.QuizName = QuizName
        self.QuizTime = QuizTime

    def json(self):
        return {"QuizID": self.QuizID, "LastUpdated": self.LastUpdated, "GradedQuiz": self.GradedQuiz,
                "PassingGrade": self.PassingGrade, "LessonID": self.LessonID, "QuizScore": self.QuizScore, "QuizName": self.QuizName, "QuizTime": self.QuizTime}

# get all quizzes in database


@app.route("/quiz")
def get_all_quizzes():
    quizlist = Quiz.query.all()
    if len(quizlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quizzes": [quiz.json() for quiz in quizlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No quiz found."
        }
    ), 404

# get quiz by lesson


@app.route("/quiz/<string:LessonID>")
def find_quiz_by_lessonID(LessonID):
    quiz = Quiz.query.filter_by(LessonID=LessonID).first()
    if quiz:
        return jsonify(
            {
                "code": 200,
                "data": quiz.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No quiz found."
        }
    ), 404

# create quiz


@app.route("/quiz/create/<string:LessonID>", methods=['POST'])
def create_quiz(LessonID):
    if (Quiz.query.filter_by(LessonID=LessonID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "lesson": LessonID
                },
                "message": "Quiz for lesson already exists."
            }
        ), 400

    data = request.get_json()
    quiz = Quiz(LessonID, **data)

    try:
        db.session.add(quiz)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "quiz": quiz.json()
                },
                "message": "An error occurred creating the quiz."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": quiz.json(),
            "message": "The quiz was successfully created."
        },
    ), 201

# delete quiz


@app.route("/quiz/delete/<string:QuizID>", methods=['DELETE'])
def delete_quiz(QuizID):
    quiz = Quiz.query.filter_by(QuizID=QuizID).first()
    if (quiz):
        try:
            db.session.delete(quiz)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred deleting the quiz."
                }
            ), 500

        return jsonify(
            {
                "code": 200,
                "message": "The quiz was successfully deleted."
            },
        ), 200

    else:
        return jsonify(
            {
                "code": 404,
                "message": "Cannot find quiz to be deleted."
            },
        ), 404


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
def get_all_trainers():
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
def find_by_trainerID(TrainerID):
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


class Material(db.Model):
    __tablename__ = 'learningmaterial'

    MaterialID = db.Column(db.Integer, primary_key=True)
    MaterialTitle = db.Column(db.String(255), nullable=False)
    MaterialDescription = db.Column(db.String(255), nullable=False)
    LessonId = db.Column(db.Integer, nullable=False)
    LastUpdated = db.Column(db.Date, nullable=False)
    MaterialURL = db.Column(db.String(255), nullable=True)
    MaterialType = db.Column(db.String(255), nullable=True)
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
def get_all_materials():
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
def find_material_by_lessonID(LessonId):
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


@app.route("/material/<string:MaterialID>", methods=['POST'])
def create_material(MaterialID):
    data = request.get_json()
    material = Material(MaterialID, **data)

    try:
        db.session.add(material)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "learningmaterial": material.json()
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

#Get single material by lessonID
@app.route("/materialSingle/<string:LessonId>")
def find_learningmaterial_by_Lesson(LessonId):
    material = Material.query.filter_by(LessonId=LessonId).first()
    if material:
        return jsonify(
            {
                "code": 200,
                "data": material.json()
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "No material found."
        }
    ), 404


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
            "message": "The question was successfully created."
        },
    ), 201

# delete questions for quiz


@app.route("/question/delete/<string:QuizID>", methods=['DELETE'])
def delete_question(QuizID):
    questions = Question.query.filter_by(QuizID=QuizID)
    if (questions):
        try:
            for qns in questions:
                db.session.delete(qns)
                db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred deleting the questions."
                }
            ), 500

        return jsonify(
            {
                "code": 200,
                "message": "The questions were successfully deleted."
            },
        ), 200

    else:
        return jsonify(
            {
                "code": 404,
                "message": "Cannot find question(s) to be deleted."
            },
        ), 404


class QuizScore(db.Model):
    __tablename__ = 'quizscore'

    EngineerID = db.Column(db.Integer, primary_key=False)
    QuizScore = db.Column(db.String(255), primary_key=False)
    LessonID = db.Column(db.Integer, primary_key=False)
    QuizID = db.Column(db.Integer, primary_key=False)
    QuizScoreID = db.Column(db.Integer, primary_key=True)


    def __init__(self,EngineerID,QuizScore,LessonID,QuizID):
        self.EngineerID = EngineerID
        self.QuizScore = QuizScore
        self.LessonID = LessonID
        self.QuizID = QuizID
 

    def json(self):
        return {"EngineerID": self.EngineerID, "QuizScore": self.QuizScore, "LessonID": self.LessonID, "QuizID": self.QuizID}


@app.route("/quizscore/create", methods=['POST'])
def create_quizscore():

    data = request.get_json()
    quizscore = QuizScore(**data)

    try:
        db.session.add(quizscore)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "quizscore": quizscore.json()
                },
                "message": "An error occurred creating the quizscore."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": quizscore.json(),
            "message": "The quizscore was successfully created."
        },
    ), 201


if __name__ == '__main__':
    app.run(debug=True)
