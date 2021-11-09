import unittest
import requests

#Done by Zi Lin
class TestClasses(unittest.TestCase):
    URL = "http://127.0.0.1:5000/class"
    data = {
        "ClassID": 1, 
        "TrainerID": 2, 
        "CourseID": 3, 
        "StartDate": "2021-10-08",
        "EndDate": "2022-04-29", 
        "StartTime": "8am", 
        "EndTime": "11am", 
        "ClassName": "Class001",
        "ClassSize": 15, 
        "ClassDay": ""}

    def testGetAllClasses(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testFindClassByTrainer(self):
        response = requests.get(self.URL + '/trainer/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testFindClassByCourseID(self):
        response = requests.get(self.URL + '/course/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)



if __name__ == "__main__":
    unittest.main()