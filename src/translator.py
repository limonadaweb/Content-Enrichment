from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound
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
            return "Traducción no disponible."
        except Exception as e:
            return f"Sucedió un error inesperado: {e}"

