from pytest import param
from page_title.file_types import FileTypes


def test_as_comment():
    arguments = "file_type, text, expected_output"
    params = [
        param(
            FileTypes.python,
            "text",
            "# text",
            id="python"
        ),
        param(
            FileTypes.js,
            "text",
            "// text",
            id="javascript"
        ),
        param(
            FileTypes.css,
            "text",
            "/* text */",
            id="css"
        ),
        param(
            FileTypes.html,
            "text",
            "<!-- text -->",
            id="html"
        ),
        param(
            FileTypes(".py"),
            "text",
            "# text",
            id="python-from-ext"
        ),
        param(
            FileTypes(".js"),
            "text",
            "// text",
            id="javascript-from-ext"
        ),
        param(
            FileTypes(".css"),
            "text",
            "/* text */",
            id="css-from-ext"
        ),
        param(
            FileTypes(".html"),
            "text",
            "<!-- text -->",
            id="html-from-ext"
        ),
    ]
    return arguments, params
