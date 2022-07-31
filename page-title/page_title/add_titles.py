from typing import TextIO
import os
import glob


def prepend_to_file(file: TextIO, text: str) -> None:
    file.seek(0, 0)
    data = file.read()
    file.seek(0, 0)
    file.write(text + "\n" + data)


def get_ext(filepath: str) -> str:
    return os.path.splitext()[-1]


def get_filepaths(root_dir: str,
                  include: list | None = None,
                  exclude: list | None = None
                  ) -> list(tuple[TextIO, str]):
    filepaths = glob.glob(root_dir, recursive=True)

    if include is not None:
        filepaths = filepaths.filter(lambda path: path in include)

    if exclude is not None:
        filepaths = filepaths.filter(lambda path: path not in exclude)

    return [(path, get_ext(path)) for path in filepaths]


def add_titles():
    pass

# TODO: find correct comment converter from extension