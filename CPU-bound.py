import concurrent.futures
from hashlib import md5
from random import choice

from benchmark import function_time


def main():
    get_coins_async(3, 61)


@function_time
def get_coins_async(count, max_workers=None):
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(get_coin) for _ in range(count)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


@function_time
def get_coins(count):
    for _ in range(count):
        print(get_coin())


def get_coin():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s, h


if __name__ == '__main__':
    main()
