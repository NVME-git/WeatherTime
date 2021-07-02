import unittest
from weatherMap import *

class TestWeatherMap(unittest.TestCase):
    """
    Tests for the weatherMap function
    """
    def test_expected_values(self):
        """
        Check the expected values for known cities
        """
        result = weatherMap('Johannesburg')
        result.pop('CurrentTemperature', None)
        expected = {
            'City':'Johannesburg',
            'CountryCode':'ZA',
            'CityTimeZone':120}
        self.assertEqual(result, expected)

        result = weatherMap('Dublin')
        result.pop('CurrentTemperature', None)
        expected = {
            'City':'Dublin',
            'CountryCode':'US',
            'CityTimeZone':-420}
        self.assertEqual(result, expected)
        
        result = weatherMap('Dublin,IE')
        result.pop('CurrentTemperature', None)
        expected = {
            'City':'Dublin',
            'CountryCode':'IE',
            'CityTimeZone':60}
        self.assertEqual(result, expected)

    def test_unexpected_values(self):
        """
        Check that unexpected requests get rejected successfully.
        """
        with self.assertRaises(Exception):
            weatherMap('Mordor')


if __name__ == '__main__':
    unittest.main()