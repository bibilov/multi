import concurrent.futures
import url_supplies

links = url_supplies.get_links()


def test(max_workers):
    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(url_supplies.load_url, url, 2): url for url in links}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                result.append('%r generated an exception: %s' % (url, exc))
            else:
                result.append('%r page is %d bytes' % (url, data))
    return result