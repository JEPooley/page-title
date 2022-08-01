from page_title.file_types import FileTypes
from typing import Callable


def as_comment(file_type: FileTypes, text: str) -> str:
    converter = get_comment_converter(file_type)
    return converter(text)


def get_comment_converter(file_type: FileTypes) -> Callable:
    if file_type == FileTypes.python:
        return as_python_comment
    elif file_type == FileTypes.js:
        return as_js_comment
    elif file_type == FileTypes.css:
        return as_css_comment
    elif file_type == FileTypes.html:
        return as_html_comment
    else:
        raise ValueError("Unrecognised File Type")


def as_python_comment(text: str) -> str: return f"# {text}"


def as_js_comment(text: str) -> str: return f"// {text}"


def as_css_comment(text: str) -> str: return f"/* {text} */"


def as_html_comment(text: str) -> str: return f"<!-- {text} -->"
