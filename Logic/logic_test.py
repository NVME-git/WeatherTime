import unittest
from logic import *

class TestLogic(unittest.TestCase):
    """
    Tests for the lambda function
    """

    def test_expected_values(self):
        """
        Check the expected values for known countries and cities
        """
        request = {
            'Country':'South Africa',
            'UserTimeZone': 120
        }
        result = lambda_handler(request,'')
        result.pop('Temperature', None)
        expected = {
            'statusCode':200,
            'reason':'OK',
            'City':'Pretoria',
            'CountryCode':'ZA',
            'TimeDifference':0
            }
        self.assertEqual(result, expected)

        request = {
            'City':'Johannesburg',
            'UserTimeZone': 0
        }
        result = lambda_handler(request,'')
        result.pop('Temperature', None)
        expected = {
            'statusCode':200,
            'reason':'OK',
            'City':'Johannesburg',
            'CountryCode':'ZA',
            'TimeDifference':-120
            }
        self.assertEqual(result, expected)

    def test_unexpected_values(self):
        """
        Check that unexpected requests get rejected successfully.
        """
        # Invalid Country
        request = {
            'Country':'ABCDEF',
            'UserTimeZone': 300
        }
        result = lambda_handler(request,'')
        expected = {
            'statusCode':404,
            'reason':'Not Found'
        }
        self.assertEqual(result, expected)

        # Invalid City
        request = {
            'City':'ABCDEF',
            'UserTimeZone': 300
        }
        result = lambda_handler(request,'')
        expected = {
            'statusCode':404,
            'reason':'Not Found'
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()