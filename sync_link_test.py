from urllib.request import Request, urlopen

import links_utils

links = links_utils.get_links()


def test():
    results=[]
    for url in links:
        try:
            results += links_utils.load_url(url, 2)
        except Exception as e:
            results += (url, e)

    return results
