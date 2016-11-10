import unittest 
from primegenerator import prime_generator

class TestPrimeGenerator(unittest.TestCase):
    
    def test_correct_input(self):
        self.assertEquals(prime_generator(13), [2, 3, 5, 7, 11, 13])
    
    def test_incorrect_data_types(self):
        with self.assertRaises(TypeError):
            prime_generator("test")
            
    def test_return_list_for_valid_input(self):
        pass
    def test_float_nums(self):
        pass
    def test_negative_numbers(self):
        pass
    def test_numbers_less_then_two(self):
        pass
    def test_with_two(self):
        pass
    def test_with_three(self):
        
if __name__ == '__main__':
    unittest.main()