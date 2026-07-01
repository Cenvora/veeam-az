from enum import Enum


class RepositoryRestorePointState(str, Enum):
    CORRUPTED = "Corrupted"
    NOTAPPLICABLE = "NotApplicable"
    OK = "Ok"

    def __str__(self) -> str:
        return str(self.value)
