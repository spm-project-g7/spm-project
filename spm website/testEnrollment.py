import unittest
import requests

#Done by Zi Lin
class TestEnrollment(unittest.TestCase):
    URL = "http://127.0.0.1:5000"
    data = {
        "CourseID": 1, 
        "ClassID": 4, 
        "EngineerID": 3, 
        "StartDate": "2021-10-08",
        "EndDate": "2022-04-29", 
        "AssignedHR": "", 
        "CourseCompleteRate": 0, 
        "CompleteStatus": "Not Complete",
        "FinalQuizScore": 0
        }
    
    def testGetAllEnrollment(self):
        response = requests.get(self.URL + '/allenrollment')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testFindByEngineer(self):
        response = requests.get(self.URL + '/class/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
    
    # def testFindByCourse(self):
    #     response = requests.get(self.URL + '/1')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), 2)

    # def testExistingSelfEnrollment(self):
    #     response = requests.post(self.URL + '/enrolself/1/3/2', json = self.data)
    #     self.assertEqual(response.status_code, 400)

    # def testSelfEnrollment(self):
    #     response = requests.post(self.URL + '/enrolself/2/2/2' , json = self.data)
    #     self.assertEqual(response.status_code, 201)

    def getEnrollmentByEngineer(self):
        response = requests.get(self.URL + '/enrollment/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def getMissingEnrollmentByEngineer(self):
        response = requests.get(self.URL + '/enrollment/9')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(response.json()), 2)

    

if __name__ == "__main__":
    unittest.main()