from .constants import WOOORDHUNT_WORD_URL


def get_validated_url(word: str) -> str:
    """
    Get the correct url to a word in wooordhunt.ru
    :param word: Url of word or word. Example (www.wooordhunt.ru/word/get or get)
    :return: url of word
    """
    if word.startswith(("https://", "wooordhunt.ru", "www.wooordhunt.ru")):
        return word
    return WOOORDHUNT_WORD_URL.format(word=word)
