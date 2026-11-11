from enum import Enum


class VirtualMachineExistsState(str, Enum):
    ALL = "All"
    ONLYDELETED = "OnlyDeleted"
    ONLYEXISTS = "OnlyExists"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
