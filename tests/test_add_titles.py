import os
import tempfile

import pytest
from page_title.add_titles import (add_titles, clean_filepath, prepend_to_file,
                                   set_first_line)

from tests.data import add_titles as data


def test_prepend_to_file():
    # Arrange
    with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
        temp_file.write("Lorem Ipsum")

        # Act
        prepend_to_file(temp_file, "Added Text")

        # Assert
        temp_file.seek(0, 0)
        file_text = temp_file.read()
        temp_file.close()
        assert file_text == "Added Text\nLorem Ipsum"


def test_set_first_line():
    # Arrange
    with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
        temp_file.write("Lorem Ipsum")

        # Act
        set_first_line(temp_file, "Added Text")

        # Assert
        temp_file.seek(0, 0)
        file_text = temp_file.read()
        temp_file.close()
        assert file_text == "Added Text\nLorem Ipsum"


def test_set_first_line_with_duplicate():
    # Arrange
    with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
        temp_file.write("Added Text\nLorem Ipsum")

        # Act
        set_first_line(temp_file, "Added Text")

        # Assert
        temp_file.seek(0, 0)
        file_text = temp_file.read()
        temp_file.close()
        assert file_text == "Added Text\nLorem Ipsum"


@pytest.mark.parametrize(*data.test_clean_filepath())
def test_clean_filepath(filepath, filename_only, expected_output):
    # Act
    cleaned_filepath = clean_filepath(filepath, filename_only)

    # Assert
    assert cleaned_filepath == expected_output


def test_add_titles_py():
    # Arrange
    with tempfile.TemporaryDirectory() as dirpath:
        path = os.path.join(dirpath, "test.py")
        with open(path, "w+") as file:
            file.write("Lorem Ipsum")
            file.seek(0, 0)

            # Act
            add_titles(dirpath)

            file.seek(0, 0)
            text = file.read()

    # Assert
    assert text == f"# {path[1:]}\nLorem Ipsum"


def test_add_titles_js():
    # Arrange
    with tempfile.TemporaryDirectory() as dirpath:
        path = os.path.join(dirpath, "test.js")
        with open(path, "w+") as file:
            file.write("Lorem Ipsum")
            file.seek(0, 0)

            # Act
            add_titles(dirpath)

            file.seek(0, 0)
            text = file.read()

    # Assert
    assert text == f"// {path[1:]}\nLorem Ipsum"
