from hashlib import md5
from random import choice,randint
import concurrent.futures

coins = [randint(0,10)]*randint(0,10)


def is_coin(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            n = s + ' ' + h
            break
    return n


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for coin in zip(executor.map(is_coin, coins)):
            print(coin)


if __name__ == '__main__':
    main()
