from enum import Enum


class CpuQuotaState(str, Enum):
    EXCEEDED = "Exceeded"
    NOISSUES = "NoIssues"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
