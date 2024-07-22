import pytest
from deep_translator.exceptions import LanguageNotSupportedException, TranslationNotFound

from src.translator import Translator


def test_translate_success():
    input_text = "Hola"
    input_tgt_lang = "en"
    input_src_lang = "es"

    my_translator = Translator(input_text, input_tgt_lang, input_src_lang)
    result = my_translator.translate()

    assert result == "Hello"


def test_translate_error():
    input_text = "fgsde"
    input_tgt_lang = "en"
    input_src_lang = "es"

    my_translator = Translator(input_text, input_tgt_lang, input_src_lang)
    result = my_translator.translate()

    assert pytest.raises(TranslationNotFound)


def test_translate_error_target_lang():
    input_text = "Python"
    input_tgt_lang = "xx"
    input_src_lang = "es"

    my_translator = Translator(input_text, input_tgt_lang, input_src_lang)
    result = my_translator.translate()

    assert pytest.raises(LanguageNotSupportedException)


def test_translate_error_src():
    input_text = "Hola"
    input_tgt_lang = "en"
    input_src_lang = "yy"

    my_translator = Translator(input_text, input_tgt_lang, input_src_lang)
    result = my_translator.translate()

    assert pytest.raises(LanguageNotSupportedException)

