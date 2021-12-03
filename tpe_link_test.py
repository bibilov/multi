import concurrent.futures

import links_utils

links = links_utils.get_links()


def test(max_workers):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(links_utils.load_url, url, 2): url for url in links}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                results += future.result()
            except Exception as e:
                results += (url, e)
    return results
