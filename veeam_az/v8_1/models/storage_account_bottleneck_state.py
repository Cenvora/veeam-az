from enum import Enum


class StorageAccountBottleneckState(str, Enum):
    NOISSUES = "NoIssues"
    THROTTLED = "Throttled"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
