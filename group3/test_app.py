import unittest
from app import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_input1Say1(self):
        result = FizzBuzz(1)
        expect = "1"
        self.assertEquals(result, expect)

if __name__ == '__main__':
    unittest.main()
