
from src.translator import TranslatorError
from src.scrape_manager import ScraperManager
from src.input_handler import InputHandler
from src.text_processor import TextProcessor
from src.filegenerator_manager import FileGeneratorManager


def main():
    api_key = ("gAAAAABmmjTMSipJboqY_lJUV3qM6dJiW1QZEOKAb0dn67H42hy3Jt4j7MpprqRkj-QrKaxzqQ"
               "-GPU_Utsd60lEiT9dU7Zyg12E7m6P64uhLiSGuX_gD9Cj7QhBOdgCrpx7lnOWtMGxK")

    scraped_data = ScraperManager.get_scraper()
    if scraped_data is None:
        print("No se encontró información sobre el tema solicitado.")
        return

    scraped_title, scraped_text = scraped_data
    text_to_translate = TextProcessor.enrich_text(scraped_text, api_key)

    tgt_lang = InputHandler.get_input_lang()
    if tgt_lang is None:
        print("Código de idioma no válido.")
        return

    try:
        translated_text = TextProcessor.translate_text(text_to_translate, tgt_lang)
        translated_title = TextProcessor.translate_text(scraped_title, tgt_lang)
        filename = InputHandler.get_filename()
        FileGeneratorManager.generate_file(filename, translated_title, translated_text)
    except TranslatorError as e:
        print(f"Error en la traducción: {e}")


if __name__ == "__main__":
    main()
