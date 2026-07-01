from enum import Enum


class StorageAccountPublicAccess(str, Enum):
    DISABLED = "Disabled"
    DONOTMODIFY = "DoNotModify"
    ENABLED = "Enabled"

    def __str__(self) -> str:
        return str(self.value)
