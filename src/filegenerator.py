class FileGenerator:
    def __init__(self, filename, *contents):
        self.filename = filename
        self.contents = contents

    def save_as_txt(self):
        while True:
            try:
                if not self.filename:
                    raise ValueError("El nombre del archivo no puede estar vacío.")
                with open(f"{self.filename}.txt", 'w', encoding='utf-8') as file:
                    for content in self.contents:
                        file.write(content + '\n\n')
                print(f"Archivo '{self.filename}.txt' se ha guardado correctamente.")
                break
            except ValueError as ve:
                print(f"Error: {ve}")
                self.filename = input("Por favor, ingresa un nombre válido(sin la extensión): ")
            except Exception as e:
                print(f"Ocurrió un error al guardar el archivo: {e}")
                break

