import pytest

from wooordhunt_parser.word import get_word


@pytest.mark.usefixtures
@pytest.mark.vcr()
async def test_get_word(word_mom, word_mom_info):
    word = await get_word(word_mom)
    assert word == word_mom_info


@pytest.mark.vcr()
async def test_get_word_with_wrong_word():
    with pytest.raises(Exception):
        await get_word("123123")
