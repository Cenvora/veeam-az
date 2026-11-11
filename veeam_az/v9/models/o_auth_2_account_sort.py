from enum import Enum


class OAuth2AccountSort(str, Enum):
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
