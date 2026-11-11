from enum import Enum


class AzureStorageFolderSort(str, Enum):
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
