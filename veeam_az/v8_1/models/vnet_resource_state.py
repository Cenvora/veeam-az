from enum import Enum


class VnetResourceState(str, Enum):
    CREATED = "Created"
    DELETED = "Deleted"
    MODIFIED = "Modified"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
