from hashlib import md5
from random import choice
import concurrent.futures
import time

import requests


def HashFinder():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            break
    return s + ' ' + h


startTime = time.time()
if __name__ == '__main__':
    i = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=32) as executor:
        futures = []
        while i < 16:
            futures.append(
                executor.submit(
                    HashFinder
                )
            )
            i = i + 1
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


print("%s sec" % (time.time() - startTime))
