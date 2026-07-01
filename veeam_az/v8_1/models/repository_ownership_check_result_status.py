from enum import Enum


class RepositoryOwnershipCheckResultStatus(str, Enum):
    HASANOTHEROWNER = "HasAnotherOwner"
    UNKNOWN = "Unknown"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
