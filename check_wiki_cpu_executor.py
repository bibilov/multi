import time
from urllib.request import Request, urlopen
from urllib.parse import unquote
start = time.time()
with open('res.txt', "r", encoding='utf8') as f:
    links = f.readlines()

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
        print(url, e)

print(f"Время работы: {time.time() - start:.3f} секунд(ы).")