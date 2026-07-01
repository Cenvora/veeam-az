from enum import Enum


class PrivateDnsSetting(str, Enum):
    DISABLED = "Disabled"
    MANAGEARECORDS = "ManageARecords"
    MANAGEAUTOMATICALLY = "ManageAutomatically"

    def __str__(self) -> str:
        return str(self.value)
