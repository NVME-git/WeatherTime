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
            'Capital':'Pretoria',
            'CountryCode':'ZA'}
        self.assertEqual(result, expected)

        result = countryCapital('Ireland')
        expected = {
            'Capital':'Dublin',
            'CountryCode':'IE'}
        self.assertEqual(result, expected)

        result = countryCapital('United States')
        expected = {
            'Capital':'Washington, D.C.',
            'CountryCode':'US'}
        self.assertEqual(result, expected)

    def test_unexpected_values(self):
        """
        Check that unexpected requests get rejected successfully.
        """
        with self.assertRaises(Exception):
            countryCapital('MORDOR')


if __name__ == '__main__':
    unittest.main()