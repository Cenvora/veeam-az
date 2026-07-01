from enum import Enum


class AzureStorageFolderState(str, Enum):
    CONTAINSREPOSITORY = "ContainsRepository"
    EMPTY = "Empty"
    NOTEMPTY = "NotEmpty"
    NOTEXIST = "NotExist"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
