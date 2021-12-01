from urllib.request import Request, urlopen
from urllib.parse import unquote
import time
import concurrent.futures

import requests

links = open('res.txt', encoding='utf8').read().split('\n')


def Checker(links):
    try:
        request = Request(
            links,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        return code
        resp.close()
    except Exception as e:
        return links, e


startTime = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for url in links:
        futures.append(
            executor.submit(
                Checker, url
            )
        )
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except requests.ConnectTimeout:
            print("ConnectTimeout.")

print("%s sec" % (time.time() - startTime))
