from src.utils.language_utils import language_dict





def get_language_code(language):
    language = language.strip().lower()
    return language_dict.get(language, None)
