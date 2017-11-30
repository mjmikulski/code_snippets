from functools import wraps

from python.elegant.elegant import elegant_numbers as en


def timing(func):
    from time import time
    @wraps(func)
    def wrap(*args, **kwargs):
        t0 = time()
        R = func(*args, **kwargs)
        wrap.t = time() - t0
        print('{} elapsed {} seconds'.format(func.__name__, en(wrap.t)))
        return R
    wrap.t = 0
    return wrap
