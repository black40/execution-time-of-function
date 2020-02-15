import timeit


def timer(func):
    def wrapper():
        try:
            start = timeit.default_timer()
            for _ in range(10):
                func()
            elapsed = (timeit.default_timer() - start) / 10
            print('Function "{name}" took {time:0.4f} second to complete.'.format(
                name=func.__name__, time=elapsed))
        except :
            print('Function "{name}" is not corect...'.format(name=func.__name__))

    return wrapper()

## ----------------EXAMPLE---------------------

@timer
def foo():
    res = [i ** 2 for i in range(200000)]
    return res

print('-' * 23)

@timer
def bad_code():
    a = 2
    b = 'spam'
    return a // b
