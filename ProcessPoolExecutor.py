import concurrent.futures, time
from hashlib import md5
from random import choice


def coin_generator(quantity):
    count = 0
    start_time = time.time()
    while count < quantity:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("0000"):
            count += 1
            print(s, h)
    print(f"Время работы: {time.time() - start_time} секунд")

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=61) as executor:
        coin_generator(5)


if __name__ == '__main__':
    main()