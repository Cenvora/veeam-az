from enum import Enum


class WorkerNetworkConfigurationType(str, Enum):
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"

    def __str__(self) -> str:
        return str(self.value)
