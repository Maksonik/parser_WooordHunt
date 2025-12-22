from bs4 import BeautifulSoup
from typing import Optional

from .constants import PART_OF_SPEECH, WOOORDHUNT_URL


def parser_word(page: str) -> dict[str:str]:
    """
    Get a detailed description of the word from page
    :param page: page text
    :return: Dictionary of word meanings
    """
    soup = BeautifulSoup(page, "lxml")
    return {
        "name": _get_word_name(soup),
        "short_description": _get_word_short_description(soup),
        "rank": _get_word_rank(soup),
        "descriptions": _get_word_descriptions(soup),
        "sounds": _get_word_sounds(soup),
        "phrases": _get_word_phrases(soup),
        "forms": _get_word_forms(soup),
    }


def _get_word_name(soup: BeautifulSoup) -> str:
    """
    Get word name
    :param soup: class BeautifulSoup of page
    :return: name of the word
    """
    if not (word_name := soup.find("h2")):
        word_name = soup.find("h1")

    return word_name.text.strip().lower()


def _get_word_short_description(soup: BeautifulSoup) -> Optional[str]:
    """
    Get a short description of the word
    :param soup: class BeautifulSoup of page
    :return: short description of the word
    """
    word_short_description = soup.find("div", "t_inline_en")
    return word_short_description.text.strip() if word_short_description else None


def _get_word_descriptions(soup: BeautifulSoup) -> list[dict]:
    """
    Get all the descriptions of the word
    :param soup: class BeautifulSoup of page
    :return: List of all meanings of the word
    """

    def _span_has_not_class(tag):
        return not tag.has_attr("class") and tag.name == "span" and not tag.text.startswith("+")

    def _get_description_info(
        part_of_speech: str,
        general_meaning: str,
        deep_meaning: str = None,
        translate: str = None,
    ) -> dict[str:str]:
        return {
            "part_of_speech": part_of_speech,
            "general_meaning": general_meaning,
            "deep_meaning": deep_meaning,
            "translate": translate,
        }

    def _get_all_general_meaning(text: str) -> list:
        general_descriptions = []
        for general_meaning in text.strip("\u2002 ").split("\u2002"):
            if not general_meaning.strip(" "):
                continue
            general_descriptions.append(
                _get_description_info(
                    part_of_speech=PART_OF_SPEECH[part_of_speech.text.strip(" ↓")],
                    general_meaning=general_meaning.strip(" "),
                )
            )
        return general_descriptions

    def _get_all_deep_meaning(text: str) -> list:
        deep_descriptions = []
        for general_meaning in text.find_next("div").find_all(_span_has_not_class):
            for br in general_meaning.find_next("div").find_all("br"):
                deep_descriptions.append(
                    _get_description_info(
                        part_of_speech=PART_OF_SPEECH[text.text.strip(" ↓")],
                        general_meaning=general_meaning.text.strip(),
                        deep_meaning=br.find_previous_sibling("i").previous_element.text.strip("\u2002—"),
                        translate=br.find_previous_sibling("i").text.strip(),
                    )
                )
        return deep_descriptions

    descriptions = []
    for part_of_speech in soup.find_all("h4"):
        text = "".join(
            str(child) for child in part_of_speech.find_next("div").contents if isinstance(child, str)
        ).replace("-", " ")

        descriptions.extend(_get_all_general_meaning(text))
        descriptions.extend(_get_all_deep_meaning(part_of_speech))
    return descriptions


def _get_word_rank(soup: BeautifulSoup) -> Optional[str]:
    """
    Get a rank of word
    :param soup: class BeautifulSoup of page
    :return: rank of word
    """
    try:
        return soup.find(id="word_rank_box").text.strip(" ")
    except Exception:
        return


def _get_word_sounds(soup: BeautifulSoup) -> list[dict]:
    """
    Get the pronunciation sounds of the word
    :param soup: class BeautifulSoup of page
    :return: list of all the pronunciation sounds of the word
    """

    def _get_sound(id: str) -> str:
        sound = ""
        if soup.find(id=id):
            sound = soup.find(id=id).text.split("   ")[:1][0]
        return sound

    def _get_url_sound(id: str) -> str:
        sound = ""
        if soup.find(id=id):
            sound = WOOORDHUNT_URL + soup.find(id=id).find("source")["src"]
        return sound

    def _get_sound_info(region: str, sound: str, sound_url: str) -> dict[str:str]:
        return {
            "region": region,
            "transcription": sound,
            "link": sound_url,
            "sound": None,
        }

    us_tr_sound = _get_sound("us_tr_sound")
    us_sound = _get_url_sound("audio_us")

    uk_tr_sound = _get_sound("uk_tr_sound")
    uk_sound = _get_url_sound("audio_uk")

    sounds = list()
    sounds.append(_get_sound_info("US", us_tr_sound, us_sound))
    sounds.append(_get_sound_info("UK", uk_tr_sound, uk_sound))
    return sounds


def _get_word_phrases(soup: BeautifulSoup) -> list[dict[str:str]]:
    """
    Get all phrases with the word
    :param soup: class BeautifulSoup of page
    :return: List of all phrases with the word
    """

    phrases = []

    if all_phrases := soup.find("div", "block phrases"):  # Fixme
        for phrase in str(all_phrases.getText).split("</span>"):
            sentense = BeautifulSoup(phrase, "lxml")
            if "—" in sentense.text:
                phrases.append(
                    {
                        "phrase": sentense.text.split(" — ")[0].strip(),
                        "translate": sentense.text.split(" — ")[1].strip(" \xa0"),
                    }
                )
    return phrases


def _get_word_forms(soup: BeautifulSoup) -> list[dict[str:str]]:
    """
    Get all forms of the word
    :param soup: class BeautifulSoup of page
    :return: List of all forms of the word
    """

    forms = []
    for form_block in soup.find_all("div", "word_form_block"):
        if not form_block.find("i"):
            continue
        part_of_speech = form_block.find("i").text
        for span in form_block.find_all("span"):
            forms.append(
                {
                    "part_of_speech": part_of_speech,
                    "condition": span.text,
                    "value": span.next_sibling.next_sibling.text.strip() if not span.next_sibling.text.strip() else "",
                }
            )
    return forms
