import unittest
from Piramida import *  
class TestPyramidNumber(unittest.TestCase):

    def test_pyramid_number(self):
        self.assertEqual(pyramid_number(1), 1)
        self.assertEqual(pyramid_number(2), 4)
        self.assertEqual(pyramid_number(3), 10)
        self.assertEqual(pyramid_number(4), 20)
        self.assertEqual(pyramid_number(5), 35)

if __name__ == '__main__':
    unittest.main()
