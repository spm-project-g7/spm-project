import unittest
import requests

#Done by Zi Lin
class TestLesson(unittest.TestCase):
    URL = "http://127.0.0.1:5000"
    data = {
        "TrainerID": 2, 
        "ClassID": 1, 
        "PrerequisiteLessonID": "", 
        "LessonName": "Lesson001"}

    def testGetAllLessons(self):
        response = requests.get(self.URL + '/lesson')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetLessonByClass(self):
        response = requests.get(self.URL + '/class/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testCreateLesson(self):
        response = requests.post(self.URL + '/lesson/9' , json = self.data)
        self.assertEqual(response.status_code, 201)

    def testGetLessonListByClass(self):
        response = requests.get(self.URL + '/lessonlist/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

if __name__ == "__main__":
    unittest.main()