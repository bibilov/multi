import time


def function_time(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(f'Время работы функции: {time.time() - start_time} сек')
        return res

    return wrapped
