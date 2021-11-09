import unittest
import requests

# Done by Ng Chun Wang
class TestLearningMaterial(unittest.TestCase):
    URL = "http://127.0.0.1:5000/material"
    data = {
        "MaterialTitle": "Course Outline",
        "MaterialDescription": "Introduction of Javascript",
        "LessonId": 6,
        "LastUpdated": "2021-10-12",
        "MaterialURL": "https://www.w3schools.com/js/DEFAULT.asp",
        "MaterialType": "URL",
        "CompleteStatus": "Not Complete"
    }

    def testGetAllLearningMaterial(self):
        response = requests.get(self.URL + 's')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetLearningMaterialListByLessonId(self):
        response = requests.get(self.URL + 's/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetLearningMaterialByLessonId(self):
        response = requests.get(self.URL + 'Single/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testPostCreateLearningMaterial(self):
        response = requests.post(self.URL + '/6' , json = self.data)
        self.assertEqual(response.status_code, 201)

    
if __name__ == "__main__":
    unittest.main()
