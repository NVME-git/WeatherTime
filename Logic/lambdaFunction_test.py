import unittest
from lambdaFunction import *

class TestLambdaFunction(unittest.TestCase):
    """
    Tests for the lambda function
    """

    def test_expected_values(self):
        """
        Check the expected values for known countries and cities
        """
        request = {
            'body': '{\r\n    "Country":"South Africa",\r\n    "UserTimeZone": 120\r\n}'
        }
        result = main(request,'')
        result = json.loads(result['body'])
        result.pop('Temperature', None)
        expected = {
            'City':'Pretoria',
            'CountryCode':'ZA',
            'TimeDifference':0}
        self.assertEqual(result, expected)

        request = {
            'body': '{\r\n    "City":"Johannesburg",\r\n    "UserTimeZone": 0\r\n}'
        }
        result = main(request,'')
        result = json.loads(result['body'])
        result.pop('Temperature', None)
        expected = {
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
            'body': '{\r\n    "Country":"ABCDEF",\r\n    "UserTimeZone": 120\r\n}'
        }
        result = main(request,'')
        self.assertEqual(result['statusCode'], 404)

        # Invalid City
        request = {
            'body': '{\r\n    "City":"ABCDEF",\r\n    "UserTimeZone": 0\r\n}'
        }
        result = main(request,'')
        expected = {
            'statusCode':404,
            'reason':'Not Found'
        }
        self.assertEqual(result['statusCode'], 404)


if __name__ == '__main__':
    unittest.main()