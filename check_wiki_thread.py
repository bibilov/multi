import time
import concurrent.futures
from urllib.request import Request, urlopen
from urllib.parse import unquote
start = time.time()
thread_count = 100
with open('res.txt', "r", encoding='utf8') as f:
    links = f.readlines()

def check_url(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)

with concurrent.futures.ThreadPoolExecutor(thread_count) as executor:
    futures = [executor.submit(check_url, url=url) for url in links]
    for future in concurrent.futures.as_completed(futures):
        future.result()

print(f"Время работы: {time.time() - start} секунд.")