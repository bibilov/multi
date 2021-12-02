import concurrent.futures
from urllib.request import Request, urlopen
from urllib.parse import unquote

links = open('res.txt', encoding='utf8').read().split('\n')


def get_link(url):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    resp = urlopen(request, timeout=5)
    code = resp.code
    print(code)
    resp.close()
    return code


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    future_to_url = {executor.submit(get_link, url): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            print(future.result())
        except Exception as e:
            print(url, e)
