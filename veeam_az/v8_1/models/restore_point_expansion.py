from enum import Enum


class RestorePointExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    REPOSITORYNAME = "RepositoryName"
    STORAGETIER = "StorageTier"
    VBRBACKUP = "VbrBackup"
    VMSNAPSHOT = "VmSnapshot"

    def __str__(self) -> str:
        return str(self.value)
