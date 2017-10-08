import unittest
from acceptance import acceptance

class isEnoughtTest(unittest.TestCase):
    def setUp(self):
        pass

    def testcase1(self):
        self.assertEqual(acceptance.acceptance("1001","58010781","1000.00"),True)
    
    def testcase2(self):
        self.assertEqual(acceptance.acceptance("1004","58010781","500.00"),False)
    
    def testcase3(self):
        self.assertEqual(acceptance.acceptance("1001","58010781","1500.00"),False)

if __name__ == '__main__':
    unittest.main()        