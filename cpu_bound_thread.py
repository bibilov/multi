import time
import random
import concurrent.futures
from hashlib import md5
worker = 100
start_time = time.time()

def generate_coin():
    while True:
        s = "".join(random.choices("0123456789", k=50))

        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s, h

with concurrent.futures.ThreadPoolExecutor(worker) as executor:
    futures = [executor.submit(generate_coin) for i in range(4)]
    for future in concurrent.futures.as_completed(futures):
        print(*future.result())

res_time = time.time() - start_time
print(f"Время работы: {res_time:.3f} секунд(ы).")