import unittest
from SimpleCalculator import Simple_Calculator
class Testsimplecalculator(unittest.testcase):
    def setUp(self):
        self.calc=Simple_Calculator()
        def test_add(self):
            self.assertEqual(self.calc.add(10,5),15)
            self.assertEqual(self.calc.add(-1,3),2)
            self.assertEqual(self.calc.add(0,-5),-5)
        def test_subtraction(self):
            self.assertEqual(self.calc.subtraction(2,2),0)
            self.assertEqual(self.calc.subtraction(5,-10),15)
            self.assertEqual(self.calc.subtraction(0,-5),5)
        def test_multiplication(self):
            self.assertEqual(self.calc.multiplication(4,4),16)
            self.assertEqual(self.calc.multipication(-5,-5),25)
            self.assertEqual(self.calc.multipication(0,23),0)
            self.assertEqual(self.calc.multipication(-4,6),-24)
        def test_division(self):
            self.assertEqual(self.calc.division(20,5),4)
            self.assertEqual(self.calc.division(-15,-3),5)
            with self.assertRaises(ValueError):
             self.calc.division(0,2)
if __name__=="__main__":
 unittest.main()

            
