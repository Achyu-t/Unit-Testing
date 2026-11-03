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




class TestMultiplyImproved(unittest.TestCase) :

    def test_with_two_positives(self):
        self.assertEqual(mainFunction.loop_multiply_improved(17,19) , 17*19)
        self.assertEqual(mainFunction.loop_multiply_improved(11677,123339) , 11677*123339)

    def test_with_one_zero(self):
        self.assertEqual(mainFunction.loop_multiply_improved(0,19) , 0)
        self.assertEqual(mainFunction.loop_multiply_improved(19,0) , 0)


    def test_with_two_zeros(self):
        self.assertEqual(mainFunction.loop_multiply_improved(0,0) , 0)

    def test_with_one_negative_number(self):
        self.assertEqual(mainFunction.loop_multiply_improved(-11 , 17) , (-11) * 17)
        self.assertEqual(mainFunction.loop_multiply_improved(11 , -17) , 11 * (-17))

    def test_with_two_negative_numbers(self):
        self.assertEqual(mainFunction.loop_multiply_improved(-11 , -17) , 11*17)
        self.assertEqual(mainFunction.loop_multiply_improved(-17 , -11) , 11 *17)




class TestIntegerLength(unittest.TestCase):

    def test_postive_numbers(self):
        self.assertEqual(mainFunction.length_of_integer(123455) , 6)
        self.assertEqual(mainFunction.length_of_integer(12) , 2)
        self.assertEqual(mainFunction.length_of_integer(1) , 1)
        self.assertEqual(mainFunction.length_of_integer(1230) , 4)

    def test_negative_numbers(self):
        self.assertEqual(mainFunction.length_of_integer(-10) , 2)
        self.assertEqual(mainFunction.length_of_integer(-123455) , 6)
        self.assertEqual(mainFunction.length_of_integer(-1) , 1)

    def test_zero(self):
        self.assertEqual(mainFunction.length_of_integer(0) , 1)

    def test_multiple_zeros(self):
        self.assertEqual(mainFunction.length_of_integer(00) , 1)
        self.assertEqual(mainFunction.length_of_integer(000) , 1)

    def test_type_mismatch(self):
        self.assertRaises(TypeError , mainFunction.length_of_integer , 'Hello')
        self.assertRaises(TypeError , mainFunction.length_of_integer , True)
        self.assertRaises(TypeError , mainFunction.length_of_integer , 123.67)
        self.assertRaises(TypeError , mainFunction.length_of_integer , '12367')
        self.assertRaises(TypeError , mainFunction.length_of_integer , [1,2,3,4])



        
if __name__ == "__main__":
    unittest.main()










# uv run python -m unittest mytest.TestMultiplyImproved to run just particular class