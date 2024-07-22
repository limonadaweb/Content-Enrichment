from src.filegenerator import FileGenerator


class FileGeneratorManager:
    @staticmethod
    def generate_file(filename, title, text):
        content = "\n".join([title, text])
        file_generator = FileGenerator(filename, content)
        file_generator.save_as_txt()
        print(f"Archivo {filename}.txt generado con éxito.")