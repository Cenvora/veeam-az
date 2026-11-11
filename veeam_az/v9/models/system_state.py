from enum import Enum


class SystemState(str, Enum):
    READY = "Ready"
    UNKNOWN = "Unknown"
    UPGRADING = "Upgrading"

    def __str__(self) -> str:
        return str(self.value)
