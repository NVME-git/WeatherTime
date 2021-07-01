import unittest
from response import *

class TestResponse(unittest.TestCase):
    """
    Tests for the response function
    """
    def test_expected_values(self):
        """
        Check the expected values for known bodies
        """
        body = {'reason':'you'}
        result = response(200, body)
        print(result)
        expected = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'},
            'isBase64Encoded' : True,
            'body' : "{\"reason\": \"you\"}"
            }

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()