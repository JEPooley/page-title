import glob
import os
import functools
from typing import Callable, TextIO

from page_title.comments import as_comment
from page_title.file_types import FileTypes


def fix_start(func) -> Callable:
    @functools.wraps(func)
    def wrapper(file, *args, **kwargs):
        file.seek(0, 0)
        result = func(file, *args, **kwargs)
        file.seek(0, 0)
        return result
    return wrapper


def prepend_to_file(file: TextIO, text: str) -> None:
    data = read_file(file)
    write_file(file, text + "\n" + data)


def set_first_line(file: TextIO, text: str) -> None:
    first_line = read_line(file)
    if first_line != text and first_line != text + "\n":
        data = read_file(file)
        write_file(file, text + "\n" + data)


@fix_start
def write_file(file: TextIO, text: str) -> None:
    file.write(text)


@fix_start
def read_file(file: TextIO) -> str:
    data = file.read()
    return data


@fix_start
def read_line(file: TextIO) -> str:
    line = file.readline()
    return line


def get_ext(filepath: str) -> str:
    return os.path.splitext(filepath)[-1]


def get_filepaths(root_dir: str,
                  include: list | None = None,
                  exclude: list | None = None
                  ) -> list[tuple[TextIO, str]]:
    filepaths = glob.glob(root_dir, recursive=True)

    if include is not None:
        filepaths = filepaths.filter(lambda path: path in include)

    if exclude is not None:
        filepaths = filepaths.filter(lambda path: path not in exclude)

    return [(path, get_ext(path)) for path in filepaths]


def add_titles(root_dir: str,
               include: list | None = None,
               exclude: list | None = None):
    filepaths = get_filepaths(root_dir, include, exclude)
    for filepath in filepaths:
        ext = get_ext(filepath)
        title = as_comment(FileTypes(ext), filepath)
        with open(filepath, "w+") as file:
            set_first_line(file, title)
