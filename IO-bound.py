import concurrent.futures
from urllib.request import urlopen

from benchmark import function_time


def main():
    links = open('res.txt', encoding='utf8').read().split('\n')
    check_links_async(links, 5, max_workers=100)


@function_time
def check_links_async(links, timeout, max_workers=None):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(get_http_status_code, url, timeout): url for url in links}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                print(future.result())
            except Exception as e:
                print(url, e)


@function_time
def check_links(links, timeout):
    for link in links:
        code = get_http_status_code(link, timeout)
        print(code)


def get_http_status_code(url, timeout):
    with urlopen(url, timeout=timeout) as resp:
        return resp.code


if __name__ == '__main__':
    main()
