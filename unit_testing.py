# --------------------------------------------
#                Unit Testing
# --------------------------------------------
import unittest
from MyPakage import msmath
from MyPakage import msstring

# print("Sum = ", msmath.sum(4, 2))
# print("multiplication = ", msmath.multiplication(4, 2))
# print("Full name: ", msstring.full_name('Hello', 'World'))

class MyPackageMSMathTestCase(unittest.TestCase):
    def test_sum(self):
        res = msmath.sum(4, 12)
        self.assertEqual(res, 16)

    def test_subtract(self):
        result = msmath.subtract(12, 2)
        self.assertEqual(result, 10)

    def test_multiplication(self):
        result = msmath.multiplication(12, 2)
        self.assertEqual(result, 24)

    def test_division(self):
        result = msmath.division(12, 2)
        self.assertEqual(result, 6)


class MyPackageMsStringTestCase(unittest.TestCase):
    def test_full_name(self):
        name = msstring.full_name('life', 'good')
        self.assertEqual('life good', name)

    def test_full_name_length(self):
        length = msstring.full_name_length('life good')
        self.assertTrue(length == 9)

    def tearDown(self):
        pass

    if __name__ == '__main__':
         unittest.main()


