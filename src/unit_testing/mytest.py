import mainFunction
import unittest

class TestMultiply(unittest.TestCase):

    def test_with_two_positives(self):
        self.assertEqual(mainFunction.loop_multiply(17,19) , 17*19)
        self.assertEqual(mainFunction.loop_multiply(11677,123339) , 11677*123339)


    ''' self.assertEqual is used to check weather two values are equal. To verify that o/p of a fxn matches the expected output.

      General Syntax :  self.assertEqual(Actual value / value to compare  , Expected value , msq = (optional message to display if test fails))
                                        (function_call , result)
    
    
    '''

    def test_with_one_zero(self):
        self.assertEqual(mainFunction.loop_multiply(0,19) , 0)
        self.assertEqual(mainFunction.loop_multiply(19,0) , 0)


    def test_with_two_zeros(self):
        self.assertEqual(mainFunction.loop_multiply(0,0) , 0)

    def test_with_one_negative_number(self):
        self.assertEqual(mainFunction.loop_multiply(-11 , 17) , (-11) * 17)
        self.assertEqual(mainFunction.loop_multiply(11 , -17) , 11 * (-17))

    def test_with_two_negative_numbers(self):
        self.assertEqual(mainFunction.loop_multiply(-11 , -17) , 11*17)
        self.assertEqual(mainFunction.loop_multiply(-17 , -11) , 11 *17)
        
        
if __name__ == "__main__":
    unittest.main()