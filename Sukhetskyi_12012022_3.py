from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*keys):
        for key in keys:
            print(f'{func.__name__}({key}: {type(key)})', end=', ')

    return wrapper


@type_logger
def calc_cube(*x):
    """asd"""
    return x ** 3


print(calc_cube.__name__)
print(calc_cube.__doc__)
print(calc_cube(3, 'fghgfh'))
