import unittest
from math import sqrt
from random import uniform
from statistics import mean

from python.pround.pround import pround


class TestElegantNumbers(unittest.TestCase):
    do_print = True

    def test_255(self):
        S = 255
        N = 10 ** 2

        xs = [uniform(0, S) for _ in range(N)]
        ys = [pround(x) for x in xs]

        m_x = mean(xs)
        m_y = mean(ys)
        delta = 2 * S / sqrt(N)

        if TestElegantNumbers.do_print:
            print('mean x: {}\nmean y: {}'.format(m_x, m_y))
            print('delta:', delta)
        self.assertAlmostEqual(m_x, m_y, delta=delta)


    def test_0_6(self):
        C = 0.6
        N = 10 ** 3

        xs = [C for _ in range(N)]
        ys = [pround(x) for x in xs]

        m_x = mean(xs)
        m_y = mean(ys)
        delta = 2 * C / sqrt(N)

        if TestElegantNumbers.do_print:
            print('mean x: {}\nmean y: {}'.format(m_x, m_y))
            print('delta:', delta)

        self.assertAlmostEqual(m_x, m_y, delta=delta)


    def test_1(self):
        S = 1
        N = 10 ** 4

        xs = [uniform(0, S) for _ in range(N)]
        ys = [pround(x) for x in xs]

        m_x = mean(xs)
        m_y = mean(ys)
        delta = 2 * S / sqrt(N)

        if TestElegantNumbers.do_print:
            print('mean x: {}\nmean y: {}'.format(m_x, m_y))
            print('delta:', delta)
        self.assertAlmostEqual(m_x, m_y, delta=delta)




if __name__ == '__main__':
    unittest.main()