



from src.filegenerator import FileGenerator



filename = input("Ingresa el nombre para el archivo que quieres generar (sin la extensión): ")
content = " Hola soy el contenido de prueba"

file_generator = FileGenerator(filename, content)
file_generator.save_as_txt()