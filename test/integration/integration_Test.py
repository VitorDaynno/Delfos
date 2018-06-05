import unittest
from app import delfos

class Test(unittest.TestCase):

    def test_get(self):
        app = delfos.test_client();   
        response = app.get('/v1/delfos/lunch?id=1&entrance=9:00')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.content_type)

if __name__ == '__main__':
    unittest.main()