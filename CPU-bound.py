import concurrent.futures
from hashlib import md5
from random import choice


def coin_gen(quantity):
    count = 0
    while count < quantity:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("0000"):
            count += 1
            print(s, h)


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        coin_gen(5)


if __name__ == '__main__':
    main()
