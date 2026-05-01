

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorator
def test(a, b):
    return a + b


print(test(1, 2, 3))
