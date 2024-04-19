from functools import wraps


def decorator_sub(symbol='-'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(symbol * 52)
            func(*args, **kwargs)
            print(symbol * 52)

        return wrapper

    return decorator
