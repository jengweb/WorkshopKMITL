import unittest
from bank import bank

class isEnoughtTest(unittest.TestCase):
    def setUp(self):
        pass

    def test50of1004isEnought(self):
        self.assertEqual(bank.sendtoBank("1004","50.00"),True)
    
    def test1000of1004isEnought(self):
        self.assertEqual(bank.sendtoBank("1004","1000.00"),False)

if __name__ == '__main__':
    unittest.main()        