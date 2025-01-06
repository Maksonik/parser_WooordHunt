from bs4 import BeautifulSoup

from constants import PART_OF_SPEECH, WOOORDHUNT_URL


def parser_word(page):
    word = {}
    soup = BeautifulSoup(page, "lxml")
    word["name"] = _set_word_name(soup)
    word["short_description"] = _set_word_short_description(soup)
    word["rank"] = _set_word_rank(soup)
    word["descriptions"] = _set_word_descriptions(soup)
    word["sounds"] = _set_word_sounds(soup)
    word["phrases"] = _set_word_phrases(soup)
    word["forms"] = _set_word_forms(soup)
    return word


def _set_word_name(soup):
    """Устанавить название слова"""
    word_name = soup.find("h2")
    if not word_name:
        word_name = soup.find("h1")

    word_name = word_name.text.strip().lower()

    return word_name


def _set_word_short_description(soup):
    """Установить короткое описание слова"""
    word_short_description = soup.find("div", "t_inline_en")
    return word_short_description.text.strip() if word_short_description else None


def _set_word_descriptions(soup):
    """Установить все значения слова"""

    def _span_has_not_class(tag):
        return (
            not tag.has_attr("class")
            and tag.name == "span"
            and not tag.text.startswith("+")
        )

    descriptions = []

    parts_of_speech = soup.find_all("h4")
    for part_of_speech in parts_of_speech:
        text = "".join(
            str(child)
            for child in part_of_speech.find_next("div").contents
            if isinstance(child, str)
        )
        text = text.replace("-", " ")
        general_meanings_with_out_deep = text.strip("\u2002 ").split("\u2002")
        for general_meaning in general_meanings_with_out_deep:
            if general_meaning.strip(" ") == "":
                continue
            descriptions.append(
                {
                    "part_of_speech": PART_OF_SPEECH[part_of_speech.text.strip(" ↓")],
                    "general_meaning": general_meaning.strip(" "),
                    "deep_meaning": None,
                    "translate": None,
                }
            )

        general_meanings = part_of_speech.find_next("div").find_all(_span_has_not_class)
        for general_meaning in general_meanings:
            brs = general_meaning.find_next("div").find_all("br")
            for br in brs:
                translate = br.find_previous_sibling("i")
                deep_meaning = translate.previous_element
                descriptions.append(
                    {
                        "part_of_speech": PART_OF_SPEECH[
                            part_of_speech.text.strip(" ↓")
                        ],
                        "general_meaning": general_meaning.text.strip(),
                        "deep_meaning": deep_meaning.text.strip("\u2002—"),
                        "translate": translate.text.strip(),
                    }
                )
    return descriptions


def _set_word_rank(soup):
    """Установить ранк слова"""
    try:
        rank = soup.find(id="word_rank_box").text.strip(" ")
    except Exception as e:
        rank = None
    return rank


def _set_word_sounds(soup):
    """Установить звуки слова"""

    sounds = []

    if soup.find(id="us_tr_sound"):
        us_tr_sound = soup.find(id="us_tr_sound").text.split("   ")[:1][0]
    else:
        us_tr_sound = ""

    if soup.find(id="uk_tr_sound"):
        uk_tr_sound = soup.find(id="uk_tr_sound").text.split("   ")[:1][0]
    else:
        uk_tr_sound = ""

    if soup.find(id="audio_us"):
        us_sound = WOOORDHUNT_URL + soup.find(id="audio_us").find("source")["src"]
    else:
        us_sound = ""

    if soup.find(id="audio_uk"):
        uk_sound = WOOORDHUNT_URL + soup.find(id="audio_uk").find("source")["src"]
    else:
        uk_sound = ""

    sounds.append(
        {
            "region": "UK",
            "transcription": uk_tr_sound,
            "link": uk_sound,
            "sound": None,
        }
    )

    sounds.append(
        {
            "region": "US",
            "transcription": us_tr_sound,
            "link": us_sound,
            "sound": None,
        }
    )

    return sounds


def _set_word_phrases(soup):
    """Установить все фразы со словом"""

    phrases = []
    all_phrases = soup.find("div", "block phrases")

    if all_phrases:
        for phrase in str(all_phrases.getText).split("</span>"):
            sentense = BeautifulSoup(phrase, "lxml")
            if "—" in sentense.text:
                translate = sentense.text.split(" — ")[1].strip(" \xa0")
                sentense = sentense.text.split(" — ")[0].strip()
                phrases.append({"phrase": sentense, "translate": translate})
    return phrases


def _set_word_forms(soup):
    """Установить все формы слова"""

    forms = []
    word_form_block = soup.find_all("div", "word_form_block")

    for form_block in word_form_block:
        part_of_speech = form_block.find("i").text
        spans = form_block.find_all("span")
        for span in spans:
            condition = span.text
            value = span.next_sibling.text.strip()
            if value == "":
                value = span.next_sibling.next_sibling.text.strip()
            forms.append(
                {
                    "part_of_speech": part_of_speech,
                    "condition": condition,
                    "value": value,
                }
            )

    return forms
