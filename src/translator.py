from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound
from deep_translator.exceptions import LanguageNotSupportedException


class TranslatorError(Exception):
    pass


class Translator:
    def __init__(self, text, tgt_lang, src_lang):
        self.text = text
        self.tgt_lang = tgt_lang
        self.src_lang = src_lang

    def translate(self):
        try:
            translated_text = GoogleTranslator(source=self.src_lang, target=self.tgt_lang).translate(self.text)
            return translated_text
        except TranslationNotFound:
            print("Traducción no disponible.")
            return TranslationNotFound
        except LanguageNotSupportedException:
            print("Idioma no admitido.")
            return LanguageNotSupportedException
        except Exception as e:
            print(f"Sucedió un error inesperado: {e}")
