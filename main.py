from src.translator import Translator
from src.wikipedia_scraper import Wikipedia_scraper


url = "https://es.wikipedia.org/wiki/"
input = "Python"
input_lang = "en"
wikipedia_scraper = Wikipedia_scraper(url, input)
scraper_text = wikipedia_scraper.scraper()[1]
#print(scraper_text)

translation = Translator(scraper_text, input_lang, "es")
print(translation.translate() + '\n')




from src.filegenerator import FileGenerator



filename = input("Ingresa el nombre para el archivo que quieres generar (sin la extensión): ")
content = " Hola soy el contenido de prueba"

file_generator = FileGenerator(filename, content)
file_generator.save_as_txt()