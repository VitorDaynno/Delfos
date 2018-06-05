import unittest
from api.bussines.delfosBO import DelfosBO

class Test(unittest.TestCase):
    
    def test_calculate_lunch_with_absent_user(self):
        delfos = DelfosBO()
        returnMethod = delfos.calculate_lunch("user-absent", "09:00")
        self.assertEqual({"message":"User not found", "code": 404}, returnMethod)
    
    def test_calculate_lunch_with_invalid_time(self):
        delfos = DelfosBO()
        returnMethod = delfos.calculate_lunch("1", "99:00")
        self.assertEqual({"message":"Invalid format time", "code": 422}, returnMethod)

    def test_calculate_lunch(self):
        delfos = DelfosBO()
        hour = delfos.calculate_lunch("1", "09:00")
        self.assertEqual("12:00", hour)   

if __name__ == '__main__':
    unittest.main()