from src.extracts import get_extr_data
import pytest


@pytest.mark.name_postprocessing
def test_remove_extra_space_punctuation():
    input_0 = "tfrhn ys jdwkhf"

    assert get_extr_data(input_0) == {
        "string": input_0,
        "count_words": 3,
        "count_vowels": 0,
        "count_consonants": 15,
    }
