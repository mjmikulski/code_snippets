from functools import wraps
import inspect


def strict_types(func):
    """
    Decorator tha provides you with dynamic type checking.
    It enforces that function is called with arguments that are exactly of annotated type.
    It checks also if value returned by the decorated function agrees with return annotation.

    There is no (even trivial) conversion.

    Known issues:
        - default arguments are not checked

    Example:

    @strict_types
    def foo(x:float, n:int, name:str='Felis catus') -> bool:
        print((name + '   ') * n)
        return x > 0.73

    foo(3.14, 3, name='Pink Panther')
    foo(3.14, n=2)
    foo(3.14, 0.25)  # -> TypeError
    foo(3.14, n=5, name=888)  # -> TypeError

    """
    @wraps(func)
    def wrap(*args, **kwargs):
        annotations = func.__annotations__
        arguments = inspect.signature(func).bind(*args, **kwargs).arguments
        for k, v in arguments.items():
            if k in annotations and type(v) is not annotations[k]:
                raise TypeError(f'As parameter \'{k}\' function got {type(v)} while {annotations[k]} was declared.')

        res = func(*args, **kwargs)

        res_type = inspect.signature(func).return_annotation
        if res_type is not inspect._empty and type(res) is not res_type:
            raise TypeError(f'Function returns {type(res)} while {res_type} was declared.')

        return res

    return wrap
