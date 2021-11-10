import unittest
import requests

#Done by Zi Lin
class TestQuizScore(unittest.TestCase):
    URL = "http://127.0.0.1:5000/quizscore"
    data = {
        "EngineerID": 1, 
        "QuizScore": "75", 
        "LessonID": 1, 
        "QuizID": 1}

    def testCreateQuizScore(self):
        response = requests.post(self.URL + '/create' , json = self.data)
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()