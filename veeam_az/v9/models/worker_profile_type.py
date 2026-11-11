from enum import Enum


class WorkerProfileType(str, Enum):
    ARCHIVE = "Archive"
    LARGE = "Large"
    MEDIUM = "Medium"
    SMALL = "Small"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
