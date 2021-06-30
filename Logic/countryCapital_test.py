import unittest
from countryCapital import *

class TestCountryCapital(unittest.TestCase):
    """
    Tests for the countryCapital function
    """

    def test_expected_values(self):
        """
        Check the expected values for known cities
        """
        result = countryCapital('South Africa')
        expected = {
            'statusCode':200,
            'reason': 'OK',
            'Capital':'Pretoria',
            'CountryCode':'ZA'}
        self.assertEqual(result, expected)

        result = countryCapital('Ireland')
        expected = {
            'statusCode':200,
            'reason': 'OK',
            'Capital':'Dublin',
            'CountryCode':'IE'}
        self.assertEqual(result, expected)

        result = countryCapital('United States')
        expected = {
            'statusCode':200,
            'reason': 'OK',
            'Capital':'Washington, D.C.',
            'CountryCode':'US'}
        self.assertEqual(result, expected)

    def test_unexpected_values(self):
        """
        Check that unexpected requests get rejected successfully.
        """
        result = countryCapital('ABCDEF')
        expected = {
            'statusCode':404,
            'reason':'Not Found'
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()