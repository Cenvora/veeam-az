from enum import Enum


class RegionSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
