from urllib.request import Request, urlopen
from urllib.parse import unquote
import time
import concurrent.futures

start_time = time.time()
threads_count = 10
with open('res.txt', "r", encoding='utf8') as f:
    links = f.readlines()


def url_check(url):
    for url in links:
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
            return links, e


with concurrent.futures.ThreadPoolExecutor(threads_count) as executor:
    futures = [executor.submit(url_check, url=url) for url in links]
    for future in concurrent.futures.as_completed(futures):
        future.result()

print("---%s seconds ---" % (time.time() - start_time))
