import requests

from parsers import parser_word
from validators import _remake_url_word_in_validated


def get_word(url_word):
    """Получить подробное описание слова"""
    correct_url = _remake_url_word_in_validated(url_word)
    page_word = get_page(correct_url)
    if page_word:
        word = parser_word(page_word)
        return word


def get_page(url_page):
    """Получить страницу слова, если данные не вставлять, то вернёт главную страницу с подразделениями слов"""
    try:
        r = requests.get(url_page)
        return r.text
    except Exception as e:
        print("Ошибка, не смог найти странциу", e)


def main():
    pass


if __name__ == "__main__":
    main()
