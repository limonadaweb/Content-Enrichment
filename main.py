from src.text_enricher import TextCortexAI
from src.translator import Translator, TranslatorError
from src.filegenerator import FileGenerator
from src.wikipedia_scraper import WikipediaScraper
from src.utils.text_utils import format_search_term, get_language_code
from urllib.parse import quote


def main():
    api_key = "gAAAAABmmjTMSipJboqY_lJUV3qM6dJiW1QZEOKAb0dn67H42hy3Jt4j7MpprqRkj-QrKaxzqQ-GPU_Utsd60lEiT9dU7Zyg12E7m6P64uhLiSGuX_gD9Cj7QhBOdgCrpx7lnOWtMGxK"
    search_term = input("Ingrese el tema a buscar: ")
    formatted_search_term = format_search_term(search_term)
    encoded_term = quote(formatted_search_term)

    url = f"https://es.wikipedia.org/wiki/{encoded_term}"

    wikipedia_scraper = WikipediaScraper(url)
    scraped_data = wikipedia_scraper.scrape()

    if scraped_data is not None:
        scraped_title, scraped_text = scraped_data
        text_to_translate = None

        input_enrich = input("¿Te interesa enriquecer el texto?: ").lower()
        if input_enrich == "si":
            text_enricher = TextCortexAI(api_key)
            text_to_translate = text_enricher.enrich_text(scraped_text)
        else:
            text_to_translate = scraped_text

        input_lang = input("Ingrese el idioma para la traducción: ")
        trgt_lang = get_language_code(input_lang)

        if trgt_lang is not None:
            try:
                translated_text = Translator(text_to_translate, trgt_lang, "es").translate()
                translated_title = Translator(scraped_title, trgt_lang, "es").translate()

                filename = input("Ingresa el nombre para el archivo que quieres generar (sin la extensión): ")
                content = "\n".join([translated_title, translated_text])

                file_generator = FileGenerator(filename, content)
                file_generator.save_as_txt()

                print(f"Archivo {filename}.txt generado con éxito.")
            except TranslatorError as e:
                print(f"Error en la traducción: {e}")
        else:
            print("Código de idioma no válido.")
    else:
        print("Error al obtener datos de Wikipedia.")


if __name__ == "__main__":
    main()
