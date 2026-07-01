from enum import Enum


class KeyVaultKeySort(str, Enum):
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
