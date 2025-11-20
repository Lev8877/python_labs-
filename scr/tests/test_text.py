import pytest
from lab03.src.lib.text import normalize, tokenize, count_freq, my_top_n


def test_normalize_basic():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("") == ""


def test_tokenize_basic():
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("") == []


def test_count_freq_and_top_n():
    assert my_top_n(count_freq(["bb", "aa", "bb", "aa", "cc"])) == [
        ("aa", 2),
        ("bb", 2),
    ]


def test_top_n_tie_breaker():
    assert my_top_n({"aa": 2, "bb": 2, "cc": 1}, ds=1) == [("aa", 2)]
    assert my_top_n({"b": 1, "a": 1}, ds=2) == [("a", 1), ("b", 1)]


# py -m pytest -q
