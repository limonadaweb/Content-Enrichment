from src.text_enricher import TextEnricher
from src.translator import Translator
from src.utils.language_utils import language_dict


class TextProcessor:
    @staticmethod
    def process_text(text, api_key):
        text_enricher = TextEnricher(api_key)
        return text_enricher.enrich_text(text)

    @staticmethod
    def get_language_code(language):
        language = language.strip().lower()
        return language_dict.get(language, None)

    @staticmethod
    def translate_text(text, target_lang):
        translator = Translator(text, target_lang, "es")
        return translator.translate()
