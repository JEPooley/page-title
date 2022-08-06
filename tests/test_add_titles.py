import tempfile
from page_title.add_titles import add_titles, prepend_to_file, set_first_line
import os


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
    assert text == f"# {path}\nLorem Ipsum"


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
    assert text == f"// {path}\nLorem Ipsum"
