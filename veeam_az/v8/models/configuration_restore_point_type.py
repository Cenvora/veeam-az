from enum import Enum


class ConfigurationRestorePointType(str, Enum):
    BYSCHEDULE = "BySchedule"
    MANUAL = "Manual"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
