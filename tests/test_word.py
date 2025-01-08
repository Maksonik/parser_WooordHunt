import pytest

from word import get_word


@pytest.mark.usefixtures
@pytest.mark.asyncio
@pytest.mark.vcr()
async def test_get_word(word_mom, word_mom_info):
    word = await get_word(word_mom)
    assert word == word_mom_info


@pytest.mark.asyncio
@pytest.mark.vcr()
async def test_get_word_with_wrong_word():
    with pytest.raises(Exception):
        asd = await get_word("123123")