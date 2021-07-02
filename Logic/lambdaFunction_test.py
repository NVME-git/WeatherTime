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
            "Country" : "South Africa",
            "UserTimeZone" : 120
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
            "City" : "Johannesburg",
            "UserTimeZone" : 0
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
            "Country" : "MORDOR",
            "UserTimeZone" : 120
        }
        result = main(request,'')
        self.assertEqual(result['statusCode'], 404)

        # Invalid City
        request = {
            "City" : "MORDOR",
            "UserTimeZone" : 0
        }
        result = main(request,'')
        expected = {
            'statusCode':404,
            'reason':'Not Found'
        }
        self.assertEqual(result['statusCode'], 404)


if __name__ == '__main__':
    unittest.main()