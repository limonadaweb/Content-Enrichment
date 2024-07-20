class InputFormatter:

    @staticmethod
    def format_search_term(search_term):
        search_term = search_term.strip()
        search_term = search_term.replace(" ", "_")
        search_term = search_term.title()
        search_term = quote(search_term)
        return search_term
