import unittest
import requests

# Done by Vanessa
class TestEngineer(unittest.TestCase):
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

    
if __name__ == "__main__":
    unittest.main()
