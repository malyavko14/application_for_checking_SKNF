import unittest
from check_SKNF_properties import check_SKNF


class Test(unittest.TestCase):

    def test1(self):
        formula = '()'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test2(self):
        formula = 'A'
        result = check_SKNF(formula)
        self.assertEqual(result, True)

    def test3(self):
        formula = '(A)'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test4(self):
        formula = '(A\/B)'
        result = check_SKNF(formula)
        self.assertEqual(result, True)

    def test5(self):
        formula = '(a\/b)'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test6(self):
        formula = '(B/\\A)'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test7(self):
        formula = 'A\/B'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test8(self):
        formula = '(A/\(!A))'
        result = check_SKNF(formula)
        self.assertEqual(result, True)

    def test9(self):
        formula = '(A\/(B\/(!C)))\/(A\/((!B)\/(!C)))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test10(self):
        formula = '(A\/B\/!C)\/(A\/B\/!C)'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test11(self):
        formula = '(A\/B\/!D)\/(A\/B\/!C)'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test12(self):
        formula = '(A\/(B\/(!C)))\/(A\/((!B)\/!C))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test13(self):
        formula = '((A\/(B\/C))/\(A\/(B\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, True)

    def test14(self):
        formula = '((A\/((!B)\/C))/\(A\/(B\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, True)

    def test15(self):
        formula = '((A\/((!B)\/C))/\((!A)\/((!B)\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, True)

    def test16(self):
        formula = '((A\/((!B)\/C))/\(A\/((!B)\/(!C)))/\((!A)\/((!B)\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, True)

    def test17(self):
        formula = '((A\/((!B)\/C))/\(A\/((!B)\/C))/\((!A)\/((!B)\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test18(self):
        formula = '((A\/((!B)\/C))/\(A\/((!B)\/C))/\((!A)\/((!B)\/(!D))))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test19(self):
        formula = '((A\/((!B)\/C))\/(A\/((!B)\/C))/\((!A)\/((!B)\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test20(self):
        formula = '((A\/((!A)\/C))/\((!A)\/((!B)\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test21(self):
        formula = '(((A)\/((!B)\/C))/\(A\/((!B)\/(!C)))/\((!A)\/((!B)\/(!C))))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test22(self):
        formula = '(A\/(!B)\/(C))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test23(self):
        formula = '(A\/(!B)\/C)'
        result = check_SKNF(formula)
        self.assertEqual(result, False)

    def test24(self):
        formula = '((A\/(D\/E)\/C))'
        result = check_SKNF(formula)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
