import pytest


class CheckWords:

    prohibited = set()

    def __init__(self, prohibited):
        self.prohibited = prohibited

    def check_for_prohibited_words(self, text: str):
        words = set(text.split(" "))
        found = words.intersection(self.prohibited)
        if found:
            for i in found:
                text = text.replace(i, "." * len(i))
        return text

    @staticmethod
    def replace_numbers_by_letters(text: str):
        text = text.replace("4", "a").replace("1", "i").replace("0", "o").replace("5", "s").replace("9","g")
        
    @staticmethod
    def sanitize(text: str):
        text = text.lower()
        text = CheckWords.replace_numbers_by_letters(text)
        return text

@pytest.fixture
def checkwords() -> CheckWords:
    prohibited = ["ass", "bitch"]
    checker = CheckWords(prohibited=prohibited)
    return checker


def test_should_remove_words_if_prohibited(checkwords: CheckWords):
    test = "Hello bitch"
    result = checkwords.check_for_prohibited_words(test)
    assert result == "Hello ....."

def test_should_remove_words_even_if_case_is_different(checkwords: CheckWords):
    test = "Hello bItCh"
    result = checkwords.check_for_prohibited_words(test)
    assert result == "Hello ....."


def should_remove_words_with_alpha_numeric_replaces():
    pass
