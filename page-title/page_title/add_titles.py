from typing import TextIO
import glob


def prepend_to_file(file: TextIO, text: str) -> None:
    file.seek(0, 0)
    data = file.read()
    file.seek(0, 0)
    file.write(text + "\n" + data)

