from hashlib import md5
from random import choice
import time

res_countCoins = 4
currCoins = 0
start_time = time.time()
while currCoins != res_countCoins:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("00000"):
        print(s, h)
        currCoins+=1
res_time = time.time() - start_time
print(f"Время работы: {res_time:.3f} секунд(ы).")