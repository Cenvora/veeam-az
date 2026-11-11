from enum import Enum


class WorkerConfigurationExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    STATUS = "Status"

    def __str__(self) -> str:
        return str(self.value)
