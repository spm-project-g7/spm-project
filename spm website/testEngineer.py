import unittest
import requests

# Done by Vanessa
class TestQuiz(unittest.TestCase):
    URL = "http://127.0.0.1:5000/engineer"
    data = {
        "EngineerID" : 2,
        "EmployeeName": "Afiq",
        "CurrentDesignation": "Senior Software Engineer",
        "Department":"Information Technology"
    }
    
  
    def testGetAllEngineers(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetAllEngineersByID(self):
        response = requests.get(self.URL + '/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetMissingEngineer(self):
        response = requests.get(self.URL + '/10')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(response.json()), 2)

    def testPostEngineer(self):
        response = requests.post(self.URL + '/create/7' , json = self.data)
        self.assertEqual(response.status_code, 201)

    def testPostExistingEngineer(self):
        response = requests.post(self.URL + '/create/7' , json = self.data)
        self.assertEqual(response.status_code, 400)

    def testDeleteEngineer(self):
        response = requests.delete(self.URL + '/delete/7' , json = self.data)
        self.assertEqual(response.status_code, 200)

    
if __name__ == "__main__":
    unittest.main()
