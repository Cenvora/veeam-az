from enum import Enum


class VnetComparisonDiffType(str, Enum):
    ADDED = "Added"
    CHANGED = "Changed"
    DELETED = "Deleted"
    UNCHANGED = "Unchanged"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
