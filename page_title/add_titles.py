import glob
import os
import functools
from typing import Callable, TextIO

from page_title.comments import as_comment
from page_title.file_types import FileTypes


def fix_start(func) -> Callable:
    """
    Resets file position to start before and after function call
    """
    @functools.wraps(func)
    def wrapper(file, *args, **kwargs):
        file.seek(0, 0)
        result = func(file, *args, **kwargs)
        file.seek(0, 0)
        return result
    return wrapper


def prepend_to_file(file: TextIO, text: str) -> None:
    """
    Adds text to the top of a file
    """
    data = read_file(file)
    write_file(file, text + "\n" + data)


def set_first_line(file: TextIO, text: str) -> None:
    """
    Inserts new text at the top of a file, unless the same text already exists
    """
    first_line = read_line(file)
    if first_line != text and first_line != text + "\n":
        data = read_file(file)
        write_file(file, text + "\n" + data)


@fix_start
def write_file(file: TextIO, text: str) -> None:
    """
    Write text to a file
    """
    file.write(text)


@fix_start
def read_file(file: TextIO) -> str:
    """
    Read text from file
    """
    data = file.read()
    return data


@fix_start
def read_line(file: TextIO) -> str:
    """
    Read first line of file
    """
    line = file.readline()
    return line


def get_ext(filepath: str) -> str:
    """
    Get file extension
    """
    return os.path.splitext(filepath)[-1]


def get_filepaths(root_dir: str,
                  include: list | None = None,
                  exclude: list | None = None
                  ) -> list[tuple[TextIO, str]]:
    """
    Get all file paths within root directory
    """
    filepaths = glob.glob(os.path.join(root_dir, "**"), recursive=True)

    if include is not None:
        filepaths = filter(lambda path: path in include, filepaths)

    if exclude is not None:
        filepaths = filter(lambda path: path not in exclude, filepaths)

    return [(path, get_ext(path)) for path in filepaths]


def strip_slashes(filepath: str) -> str:
    """
    Remove prevailing forward slashes and dot-slashes from filepath
    """
    if filepath[:2] == "./":
        return filepath[2:]
    elif filepath[0] == "/":
        return filepath[1:]
    return filepath


def clean_filepath(filepath: str, filename_only: bool = False) -> str:
    """
    Trim unnecessary slashes and convert to forward slashes
    """
    filepath = filepath.replace("\\", "/")
    filepath = strip_slashes(filepath)
    if filename_only:
        _, filepath = os.path.split(filepath)
    return filepath


def add_titles(root_dir: str,
               include: list | None = None,
               exclude: list | None = None,
               filename_only: bool = False):
    """
    Add filename or filepath as a commented title to all files within the root
    directory
    """
    filepaths = get_filepaths(root_dir, include, exclude)
    for filepath, ext in filepaths:
        if ext in (".py", ".js", ".html", ".css"):
            title = clean_filepath(filepath, filename_only)
            comment = as_comment(FileTypes(ext), title)
            with open(filepath, "r+") as file:
                set_first_line(file, comment)
