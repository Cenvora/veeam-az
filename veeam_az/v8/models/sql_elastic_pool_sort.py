from enum import Enum


class SqlElasticPoolSort(str, Enum):
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
