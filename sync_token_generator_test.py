import tokens


def test(tokens_num):
    return [tokens.get_token() for _ in range(0, tokens_num)]
