from src.input_handler import InputHandler
from src.text_enricher import TextEnricher
from src.translator import Translator


class TextProcessor:
    @staticmethod
    def enrich_text(text, api_key):
        if InputHandler.should_enrich_text():
            text_enricher = TextEnricher(api_key)
            text_to_translate = text_enricher.enrich_text(text)
        else:
            text_to_translate = text
        return text_to_translate

    @staticmethod
    def translate_text(text, target_lang):
        translator = Translator(text, target_lang, "es")
        return translator.translate()
