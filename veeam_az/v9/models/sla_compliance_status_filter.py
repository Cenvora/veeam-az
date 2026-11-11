from enum import Enum


class SlaComplianceStatusFilter(str, Enum):
    ALL = "All"
    METSLA = "MetSla"
    MISSEDSLA = "MissedSla"
    REMOVED = "Removed"

    def __str__(self) -> str:
        return str(self.value)
