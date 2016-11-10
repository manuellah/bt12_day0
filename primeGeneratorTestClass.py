import unittest 
from primegenerator import prime_generator

class TestPrimeGenerator(unittest.TestCase):
    
    def test_correct_input(self):
        self.assertEquals(prime_generator(13), [2, 3, 5, 7, 11, 13])
        
if __name__ == '__main__':
    unittest.main()