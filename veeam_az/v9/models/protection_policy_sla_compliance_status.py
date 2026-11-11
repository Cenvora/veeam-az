from enum import Enum


class ProtectionPolicySlaComplianceStatus(str, Enum):
    METSLA = "MetSla"
    MISSEDSLA = "MissedSla"
    NOTEXECUTED = "NotExecuted"

    def __str__(self) -> str:
        return str(self.value)
