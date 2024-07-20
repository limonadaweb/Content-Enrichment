from src.input_handler import InputHandler
from src.wikipedia_scraper import WikipediaScraper


class ScraperManager:
    @staticmethod
    def get_scraper():
        search_input = InputHandler.get_search_term()
        wikipedia_scraper = WikipediaScraper(search_input)
        return wikipedia_scraper.scrape()
