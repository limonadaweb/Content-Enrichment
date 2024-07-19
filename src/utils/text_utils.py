from src.utils.language_utils import language_dict


def format_search_term(term):
    term = term.strip()
    term = term.replace(" ", "_")
    term = term.title()
    return term


def get_language_code(language):
    language = language.strip().lower()
    return language_dict.get(language, None)
