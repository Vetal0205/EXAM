import unittest
from Piramida import pyramid_number

class TestPyramidNumber(unittest.TestCase):

    def test_pyramid_number_correct(self):
        self.assertEqual(pyramid_number(1), 1)
        self.assertEqual(pyramid_number(2), 4)
        self.assertEqual(pyramid_number(3), 10)

    def test_pyramid_number_incorrect(self):
        self.assertNotEqual(pyramid_number(1), 0)
        self.assertNotEqual(pyramid_number(2), 5)

    def test_pyramid_number_positive(self):
        self.assertTrue(pyramid_number(1) > 0)
        self.assertTrue(pyramid_number(10) > 0)

    def test_pyramid_number_zero(self):
        self.assertEqual(pyramid_number(0), 0)

    def test_pyramid_number_negative(self):
        with self.assertRaises(ValueError):
            pyramid_number(-1)

if __name__ == '__main__':
    unittest.main()
