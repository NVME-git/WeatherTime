import unittest
from timeZone import timeZone

class TestTimeZone(unittest.TestCase):
    """
    Tests for the validTimeZone function
    """
    def test_expected_values(self):
        """
        Check the expected values for valid time zones
        """
        self.assertEqual(timeZone('0'), 0)
        self.assertEqual(timeZone('60'), 1)
        self.assertEqual(timeZone('-60'), -1)
        self.assertEqual(timeZone('360'), 6)
        self.assertEqual(timeZone('-360'), -6)

    def test_unexpected_values(self):
        """
        Check that unexpected requests get rejected successfully.
        """
        with self.assertRaises(Exception):
            timeZone(str(-12*60))
        with self.assertRaises(Exception):
            timeZone(str(15*60))
        with self.assertRaises(Exception):
            timeZone('sixty')



if __name__ == '__main__':
    unittest.main()