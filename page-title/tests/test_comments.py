import pytest
from page_title.comments import as_comment

from tests.data import comments as data


@pytest.mark.parametrize(*data.test_as_comment())
def test_as_comment(file_type, text, expected_output):
    # Act
    comment = as_comment(file_type, text)

    # Assert
    assert comment == expected_output
