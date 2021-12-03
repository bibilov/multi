import url_supplies

links = url_supplies.get_links()


def test():
    result = []
    for url in links:
        try:
            result.append(url_supplies.load_url(url, 2))
        except Exception as e:
            result.append((url, e))
    return result
