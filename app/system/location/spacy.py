import re
from typing import get_args, Iterable, Literal

import spacy


Location = tuple[str, int]


MAX_PROCESSING_SIZE = 10000
PROCESSING_GRACE = 100

BOUNDARY = re.compile(r"\b")

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


def get_raw_locations(
        nlp: spacy.language.Language,
        chunk: Location) -> Iterable[tuple[str, int, int]]:
    text, offset = chunk
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ not in ["LOC", "GPE"]:
            continue
        yield (ent.text, ent.start_char + offset, ent.end_char + offset)


def next_chunk(text: str, offset: int) -> tuple[Location, Location | None]:
    if len(text) < MAX_PROCESSING_SIZE:
        return (text, offset), None
    bix = MAX_PROCESSING_SIZE
    boundary = BOUNDARY.search(
        text,
        MAX_PROCESSING_SIZE - PROCESSING_GRACE,
        MAX_PROCESSING_SIZE + PROCESSING_GRACE)
    if boundary is not None:
        bix = boundary.start() - 1
    fix = bix + PROCESSING_GRACE
    boundary = BOUNDARY.search(text, bix, bix + PROCESSING_GRACE)
    if boundary is not None:
        fix = boundary.start() - 1
    chunk = text[:fix]
    remain = text[bix:]
    print(f"chunk: '...{chunk[:-150]}'\nremain: '{remain[:150]}...'")
    return (chunk, offset), (remain, offset + bix)


def get_locations(
        nlp: spacy.language.Language,
        text: str) -> Iterable[tuple[str, int, int]]:
    overlap_end = 0

    def get_overlap_end(chunk: Location) -> int:
        cur_text, cur_offset = chunk
        return cur_offset + len(cur_text)

    next_offset = 0
    next_text = text
    buff: list[tuple[str, int, int]] = []
    while True:
        chunk, remain = next_chunk(next_text, next_offset)
        next_buff = list(get_raw_locations(nlp, chunk))
        overlaps = {
            start
            for (_, start, _) in next_buff
            if start < overlap_end
        }
        yield from (
            hit
            for hit in buff
            if hit[1] not in overlaps
        )
        if remain is None:
            break
        buff = next_buff
        overlap_end = get_overlap_end(chunk)
        next_text, next_offset = remain
    yield from next_buff
