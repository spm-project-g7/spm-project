import unittest
import requests

#Done by Yuheng
class TestTrainer(unittest.TestCase):
    URL = "http://127.0.0.1:5000/trainer"
    data = {
        "TrainerID" : 1,
        "EmployeeName": "Nova Choi",
        "CurrentDesignation": "Senior Admin",
        "Department": "Staff Development"
    }

    def testGetAllTrainers(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testFindTrainerByID(self):
        response = requests.get(self.URL + '/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetMissingTrainer(self):
            response = requests.get(self.URL + '/10')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(len(response.json()), 2)
    

if __name__ == "__main__":
    unittest.main()