from enum import Enum


class StandardAccountExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    SERVERS = "Servers"

    def __str__(self) -> str:
        return str(self.value)
