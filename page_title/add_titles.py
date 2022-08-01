import glob
import os
from typing import TextIO

from page_title.comments import as_comment
from page_title.file_types import FileTypes


def prepend_to_file(file: TextIO, text: str) -> None:
    file.seek(0, 0)
    data = file.read()
    file.seek(0, 0)
    file.write(text + "\n" + data)


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
            prepend_to_file(file, title)
