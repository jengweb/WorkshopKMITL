import unittest
from wallet import wallet

class isEnoughtTest(unittest.TestCase):
    def setUp(self):
        pass

    def test1000of58010781isEnought(self):
        self.assertEqual(wallet.isEnought("58010781","1000.00"),True)
    
    def test1500of58010781isEnought(self):
        self.assertEqual(wallet.isEnought("58010781","1500.00"),False)

if __name__ == '__main__':
    unittest.main()        