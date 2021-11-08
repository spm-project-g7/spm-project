import unittest
import requests

#Done by Zi Lin
class TestCourse(unittest.TestCase):
    URL = "http://127.0.0.1:5000/course"
    data = {
        "CourseID" : 3,
        "CourseName": "Internet Security",
        "CourseValidStartDate": "2021-10-08",
        "CourseValidEndDate": "	2032-10-31",
        "CreatedBy": 1
    }

    def testGetAllCourses(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testFindCourseByID(self):
        response = requests.get(self.URL + '/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def testGetMissingCourse(self):
            response = requests.get(self.URL + '/10')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(len(response.json()), 2)
    

if __name__ == "__main__":
    unittest.main()