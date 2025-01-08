import pytest


@pytest.fixture
def word_mom():
    return "mom"


@pytest.fixture
def word_mom_url():
    return f"https://wooordhunt.ru/word/mom"


@pytest.fixture
def word_mom_info():
    return {'name': 'mom', 'short_description': 'мама', 'rank': '1 042', 'descriptions': [{'part_of_speech': 'noun', 'general_meaning': 'мама', 'deep_meaning': None, 'translate': None}], 'sounds': [{'region': 'UK', 'transcription': ' амер.\xa0  |mɑːm|', 'link': 'https://wooordhunt.ru//data/sound/sow/us/mom.mp3', 'sound': None}, {'region': 'UK', 'transcription': ' брит.\xa0  |mɒm|', 'link': 'https://wooordhunt.ru//data/sound/sow/uk/mom.mp3', 'sound': None}], 'phrases': [{'phrase': 'mom-and-pop shop', 'translate': 'амер. мелкое частное предпринимательство'}, {'phrase': 'deadbeat dad / mom', 'translate': 'неплательщик / неплательщица алиментов'}, {'phrase': 'mom and dad', 'translate': 'родители; предки'}, {'phrase': 'mom-and-pop firm', 'translate': 'мелкая семейная фирма; семейная фирма'}, {'phrase': 'mom and pop outlets', 'translate': 'семейный магазин'}, {'phrase': 'mom and pop', 'translate': 'семейный'}, {'phrase': 'mom-and-pop', 'translate': 'относящийся к не большому семейному бизнесу; материнский; отцовский'}], 'forms': [{'part_of_speech': 'noun', 'condition': 'ед. ч.(singular):', 'value': ''}, {'part_of_speech': 'noun', 'condition': 'мн. ч.(plural):', 'value': 'moms'}]}
