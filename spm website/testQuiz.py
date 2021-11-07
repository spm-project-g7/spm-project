import unittest
import requests

# Done by Yuanyuan
class TestQuiz(unittest.TestCase):
    URL = "http://127.0.0.1:5000/quiz"
    data = {
        "LastUpdated": "2021-10-12",
        "GradedQuiz": 0,
        "PassingGrade": 50,
        "LessonID": 7,
        "QuizScore": 100,
        "QuizName": "Quiz007",
        "QuizTime": 60
    }

    def testGetAllQuizzes(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetAllQuizzesByLesson(self):
        response = requests.get(self.URL + '/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetMissingQuiz(self):
        response = requests.get(self.URL + '/10')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(response.json()), 2)

    def testPostQuiz(self):
        response = requests.post(self.URL + '/create/7' , json = self.data)
        self.assertEqual(response.status_code, 201)
    
if __name__ == "__main__":
    unittest.main()
