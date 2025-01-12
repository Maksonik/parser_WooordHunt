import httpx

from .parsers import parser_word
from .validators import get_validated_url


async def get_word(url_word: str) -> dict[str:str]:
    """
    Get a detailed description of the word
    :param url_word: Url of word or word. Example (www.wooordhunt.ru/word/get or get)
    :return: Dictionary of word meanings
    """
    correct_url = get_validated_url(url_word)
    page_word = await get_page(correct_url)
    if page_word:
        word = parser_word(page_word)
        return word


async def get_page(url: str) -> str:
    """
    Get word page
    :param url: url of word
    :return: Page text
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return response.text
    except Exception as e:
        raise e

