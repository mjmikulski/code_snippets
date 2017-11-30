from functools import wraps

def nothrow(msg='error'):
    def nothrow_(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            R = None
            try:
                R = f(*args, **kwargs)
            except Exception  as err:
                wrap.errors += 1
                print('{}:{}\n{}'.format(f.__name__, msg, err))
            return R
        wrap.errors = 0
        return wrap
    return  nothrow_