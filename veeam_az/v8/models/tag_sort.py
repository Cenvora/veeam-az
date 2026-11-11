from enum import Enum


class TagSort(str, Enum):
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    VALUEASC = "ValueAsc"
    VALUEDESC = "ValueDesc"

    def __str__(self) -> str:
        return str(self.value)
