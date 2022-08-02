import tempfile

from page_title.add_titles import prepend_to_file, set_first_line


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
