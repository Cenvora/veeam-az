from enum import Enum


class SlaComplianceStatus(str, Enum):
    METSLA = "MetSla"
    MISSEDSLA = "MissedSla"
    REMOVED = "Removed"

    def __str__(self) -> str:
        return str(self.value)
