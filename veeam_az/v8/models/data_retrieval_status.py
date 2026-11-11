from enum import Enum


class DataRetrievalStatus(str, Enum):
    NONE = "None"
    RETRIEVED = "Retrieved"
    RETRIEVING = "Retrieving"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
