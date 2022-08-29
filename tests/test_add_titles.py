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


@pytest.mark.parametrize(*data.test_add_titles())
def test_add_titles(extension, file_text, comment_prefix, comment_suffix):
    # Arrange
    with tempfile.TemporaryDirectory() as dirpath:
        path = os.path.join(dirpath, "test" + extension)
        with open(path, "w+") as file:
            file.write(file_text)
            file.seek(0, 0)

            # Act
            add_titles(dirpath)

            file.seek(0, 0)
            text = file.read()

    # Assert
    assert text == f"{comment_prefix}{path[1:]}{comment_suffix}\n{file_text}"


@pytest.mark.parametrize(*data.test_add_titles())
def test_add_titles_filename_only(extension, file_text,
                                  comment_prefix, comment_suffix):
    # Arrange
    with tempfile.TemporaryDirectory() as dirpath:
        filename = "test" + extension
        path = os.path.join(dirpath, filename)
        with open(path, "w+") as file:
            file.write(file_text)
            file.seek(0, 0)

            # Act
            add_titles(dirpath, filename_only=True)

            file.seek(0, 0)
            text = file.read()

    # Assert
    assert text == f"{comment_prefix}{filename}{comment_suffix}\n{file_text}"
