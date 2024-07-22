import os
import pytest
from src.filegenerator import FileGenerator


def test_save_as_txt_creates_filename(tmpdir):
    temp_file = tmpdir.join("testfile")
    filename = temp_file.strpath
    content = "este es el contenido de prueba"

    file_generator = FileGenerator(filename, content)
    file_generator.save_as_txt()

    assert os.path.exists(f"{filename}.txt")
    with open(f"{filename}.txt", 'r', encoding='utf-8') as file:
        assert file.read().strip() == content.strip().lower()


def test_save_as_txt_not_filename_provide(tmpdir):
    temp_file = tmpdir.join("")
    filename = temp_file.strpath
    content = "este es el contenido de prueba"

    file_generator = FileGenerator(filename, content)
    file_generator.save_as_txt()

    assert pytest.raises(ValueError)
