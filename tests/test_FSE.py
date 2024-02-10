import unittest

class ActivityTests(unittest.TestCase):
    def check_api_request(self):
        """Check the API key value and the connection with data"""

    def test_city_exist(self):
        """City and the size of letters"""
        self.assertTrue(
            find_city_and_airport('PAris')
        )

if __name__ == '__main__':
    unittest.main()