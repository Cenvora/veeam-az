from enum import Enum


class VirtualMachineSnapshotExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    RESTOREPOINT = "RestorePoint"

    def __str__(self) -> str:
        return str(self.value)
