import concurrent.futures

import tokens


def test(tokens_num, max_workers):
    result = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(tokens.get_token) for _ in range(0, tokens_num)]
        for future in concurrent.futures.as_completed(futures):
            result += future.result()
    return result
