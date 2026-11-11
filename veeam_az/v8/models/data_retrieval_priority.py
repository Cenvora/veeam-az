from enum import Enum


class DataRetrievalPriority(str, Enum):
    HIGH = "High"
    NORMAL = "Normal"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
