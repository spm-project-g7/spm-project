import unittest
import requests

#Done by Zi Lin
class TestQuestion(unittest.TestCase):
    URL = "http://127.0.0.1:5000/question"
    data = {
        
        "QuestionID": 1, 
        "Options": "True,False", 
        "Answer": 0, 
        "Question": "Is the number after 2, 3?"}

    def testGetAllQuestions(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetQuestionByQuizID(self):
        response = requests.get(self.URL + '/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testCreateQuestion(self):
        response = requests.post(self.URL + '/create/9' , json = self.data)
        self.assertEqual(response.status_code, 201)

    def testDeleteQuestion(self):
        response = requests.delete(self.URL + '/delete/9' , json = self.data)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()