from typing import get_args, Iterable, Literal

import spacy


Language = Literal["en"]
LANGUAGES = get_args(Language)


SPACY_NLP: spacy.language.Language | None = None


def get_spacy(language: Language) -> spacy.language.Language:
    global SPACY_NLP

    if language not in LANGUAGES:
        raise ValueError(f"unknown language ({LANGUAGES}): {language}")
    if SPACY_NLP is None:
        SPACY_NLP = spacy.load("en_core_web_sm")
    return SPACY_NLP


def get_locations(
        nlp: spacy.language.Language,
        text: str) -> Iterable[tuple[str, int, int]]:
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ not in ["LOC", "GPE"]:
            continue
        yield (ent.text, ent.start, ent.end)
