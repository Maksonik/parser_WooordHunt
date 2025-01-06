import httpx
# import asyncio

from parsers import parser_word
from validators import get_validated_url


def get_word(url_word):
    """Получить подробное описание слова"""
    correct_url = get_validated_url(url_word)
    page_word = get_page(correct_url)
    if page_word:
        word = parser_word(page_word)
        return word


async def get_page(url_page):
    """Получить страницу слова, если данные не вставлять, то вернёт главную страницу с подразделениями слов"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url_page)
        return response.text
    except Exception as e:
        print("Ошибка, не смог найти странциу", e)


# async def main():
#     print(await get_page("https://wooordhunt.ru/word/get"))
#
# asyncio.run(main())
