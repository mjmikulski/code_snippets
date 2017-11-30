import unittest

from python.decor.nothrow import nothrow
from python.decor.err_hist import ErrorHistory
from python.decor.timing import timing



class TestNothrow(unittest.TestCase):
    def test_division(self):
        @nothrow(msg='dupa zbita')
        def div(x):
            return 1 / x

        y = []
        for x in [-1,0,1,0]:
            y.append(div(x))
        self.assertEqual(y, [-1, None, 1, None])
        self.assertEqual(div.errors, 2)

    def test_open(self):
        @nothrow()
        def open_nothrow(*args, **kwargs):
            return open(*args, **kwargs)

        open_nothrow(file='foo')

    def test_history(self):
        @ErrorHistory
        def faulty(x):
            if x == 1:
                raise ValueError('x=1')
            if x == 2:
                raise TypeError('x=2')
            if x == 3:
                raise IOError('x=3')
        for x in range(5):
            faulty(x)
        faulty.show_errors()
        faulty.reset()
        faulty.show_errors()


class TestTiming(unittest.TestCase):
    def test_simple(self):
        @timing
        def just_wait():
            from time import sleep
            sleep(1)
        just_wait()

        self.assertAlmostEqual(just_wait.t, 1, delta=1.E-2)

























if __name__ == '__main__':
    unittest.main()


