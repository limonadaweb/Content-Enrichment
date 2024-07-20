class InputHandler:
    @staticmethod
    def get_serach_term():
        search_term = input("Ingrese el tema a buscar: ")
        return search_term

    @staticmethod
    def get_filename():
        filename = input("Ingrese el nombre del archivo: ")
        return filename

    @staticmethod
    def get_input_lang():
        input_lang = input("Ingrese el idioma para la traducción: ")
        tgt_lang = get_language_code(input_lang)
        return tgt_lang

    @staticmethod
    def should_enrich_text():
        answer = input("¿Te interesa enriquecer el texto? (si/no): ").lower().strip()
        if answer == "si":
            return True
        else:
            return False
