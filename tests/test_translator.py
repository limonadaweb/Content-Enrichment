import pytest
from behave import *
from src.translator import Translator


def test_translate_success():
    input_text = "Hola"
    input_tgt_lang = "en"
    input_src_lang = "es"

    my_translator = Translator(input_text, input_tgt_lang, input_src_lang)
    result = my_translator.translate()

    assert result == "Hello"
