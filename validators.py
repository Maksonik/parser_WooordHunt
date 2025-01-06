from constants import WOOORDHUNT_WORD_URL


def _remake_url_word_in_validated(url_word):
    """Видоизменить ссылку на правильную"""
    if url_word.startswith(("https://", "wooordhunt.ru", "www.wooordhunt.ru")):
        return url_word
    return WOOORDHUNT_WORD_URL.format(word=url_word)
