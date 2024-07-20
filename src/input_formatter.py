from urllib.parse import quote
from src.utils.language_utils import language_dict


class InputFormatter:

    @staticmethod
    def format_search_term(search_term):
        search_term = search_term.strip()
        search_term = search_term.replace(" ", "_")
        search_term = search_term.title()
        search_term = quote(search_term)
        return search_term

    @staticmethod
    def get_language_code(language):
        language = language.strip().lower()
        return language_dict.get(language, None)
