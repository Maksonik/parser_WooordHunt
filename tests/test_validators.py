import pytest

from wooordhunt_parser import get_validated_url


@pytest.mark.usefixtures
def test_get_validated_url_with_word(word_mom):
    assert get_validated_url(word_mom) == "https://wooordhunt.ru/word/mom"


@pytest.mark.usefixtures
def test_get_validated_url_with_url(word_mom_url):
    assert get_validated_url(word_mom_url) == word_mom_url
