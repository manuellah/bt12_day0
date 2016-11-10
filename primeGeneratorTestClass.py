import unittest 
from primegenerator import prime_generator

class TestPrimeGenerator(unittest.TestCase):
    
    def test_correct_input(self):
        self.assertEquals(prime_generator(13), [2, 3, 5, 7, 11, 13])
    
    def test_incorrect_data_types(self):
        with self.assertRaises(TypeError):
            prime_generator("test")
            
    def test_return_list_for_valid_input(self):
        
    def test_float_nums(self):
        pass
    def test_negative_numbers(self):
        self.assertEqual(prime_generator(-12), "The number has to be greater than 1")
    def test_numbers_less_then_two(self):
        pass
    def test_with_one(self):
        self.assertEqual(prime_generator(1), "The number has to be greater than 1")
    
    def test_with_two(self):
        self.assertEqual(prime_generator(2), [2])
    def test_with_three(self):
        self.assertEqual(prime_generator(3), [2, 3])
    
        
if __name__ == '__main__':
    unittest.main()