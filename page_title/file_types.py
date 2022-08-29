from enum import Enum
from functools import cache


class FileTypes(Enum):
    python = ".py"
    js = ".js"
    css = ".css"
    html = ".html"

    @classmethod
    @cache
    def list_values(cls) -> list:
        return list(map(lambda c: c.value, cls))
