from hashlib import md5
from random import choice, randint
import concurrent.futures


def is_coin(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ' ' + h


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for coin in zip(executor.map(is_coin, range(9))):
            print(coin)


if __name__ == '__main__':
    main()
