import unittest
from math import pi, log

from python.elegant.elegant import elegant_numbers as en


class TestElegantNumbers(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(en(0), '0')
        self.assertEqual(en(0, zero_sign=''), '')
        self.assertEqual(en(0, zero_sign='#'), '#')

    def test_moderate_small(self):
        self.assertEquals(en(0.1), '0.100')
        self.assertEquals(en(-0.1234), '-0.123')
        self.assertEquals(en(+17.19), '17.2')
        self.assertEquals(en(21.9921234), '22.0')
        self.assertEquals(en(995.78901), '996')

    def test_integers(self):
        self.assertEquals(en(12), '12')
        self.assertEquals(en(1989), '1989')
        self.assertEquals(en(32789), '3.28e+4')
        self.assertEquals(en(-333), '-333')

    def test_big(self):
        self.assertEquals(en(7.1 ** 7), '9.10e+5')

    def test_small(self):
        self.assertEquals(en(-7.1 ** -7), '-1.10e-6')

    def test_n(self):
        self.assertEquals(en(pi), '3.14')
        self.assertEquals(en(pi, n=6), '3.14159')
        self.assertEquals(en(pi, n=5), '3.1416')
        self.assertEquals(en(pi ** (-10), n=4), '1.068e-5')
        self.assertEquals(en(pi ** (-10), n=2), '1.1e-5')
        self.assertRaises(TypeError, en, pi, n=0.5)
        self.assertRaises(ValueError, en, pi, n=0)

    def test_leading_zeros(self):
        self.assertEquals(en(-0.05128117), '-0.0513')
        self.assertEquals(en(-0.5128117, max_leading_zeros=0), '-5.13e-1')
        self.assertEquals(en(-0.005128117), '-5.13e-3')
        self.assertEquals(en(-0.0005128117, max_leading_zeros=5), '-0.000513')


    def test_leading_nonzeros(self):
        self.assertEquals(en(2017), '2017')
        self.assertEquals(en(2017, max_leading_nonzeros=2), '2.02e+3')

        self.assertEquals(en(12345), '1.23e+4')
        self.assertEquals(en(12345, max_leading_nonzeros=6), '12345')

    def test_exponent_mark(self):
        self.assertEquals(en(7**7, n=2), '8.2e+5')
        self.assertEquals(en(7**7, n=2, exponent_mark='D'), '8.2D+5')

    def test_nan(self):
        self.assertEquals(en('foo'), 'foo')
        self.assertEquals(en('foo', nan_sign='###'), '###')


if __name__ == '__main__':
    unittest.main()