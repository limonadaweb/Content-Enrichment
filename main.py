from src.input_formatter import InputFormatter
from src.translator import TranslatorError
from src.wikipedia_scraper import WikipediaScraper
from src.input_handler import InputHandler
from src.text_processor import TextProcessor
from src.filegenerator_manager import FileGeneratorManager


def main():
    api_key = ("gAAAAABmmjTMSipJboqY_lJUV3qM6dJiW1QZEOKAb0dn67H42hy3Jt4j7MpprqRkj-QrKaxzqQ"
               "-GPU_Utsd60lEiT9dU7Zyg12E7m6P64uhLiSGuX_gD9Cj7QhBOdgCrpx7lnOWtMGxK")
    search_input = InputHandler.get_serach_term()
    search_input = InputFormatter.format_search_term(search_input)
    wikipedia_scraper = WikipediaScraper(search_input)
    scraped_data = wikipedia_scraper.scrape()

    if scraped_data is None:
        print("No se encontró información sobre el tema solicitado.")
        return

    scraped_title, scraped_text = scraped_data
    if InputHandler.should_enrich_text():
        text_to_translate = TextProcessor.process_text(scraped_text, api_key)
    else:
        text_to_translate = scraped_text

    tgt_lang = InputHandler.get_input_lang()
    if tgt_lang is None:
        print("Código de idioma no válido.")
        return

    try:
        translated_text = TextProcessor.translate_text(text_to_translate, target_lang)
        translated_title = TextProcessor.translate_text(scraped_title, target_lang)

        filename = InputHandler.get_filename()
        FileGeneratorManager.generate_file(filename, translated_title, translated_text)
    except TranslatorError as e:
        print(f"Error en la traducción: {e}")


if __name__ == "__main__":
    main()
