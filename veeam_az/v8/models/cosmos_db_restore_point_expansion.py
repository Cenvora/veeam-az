from enum import Enum


class CosmosDbRestorePointExpansion(str, Enum):
    NONE = "None"
    REPOSITORYNAME = "RepositoryName"
    RESTORABLERESOURCES = "RestorableResources"
    STORAGETIER = "StorageTier"
    VBRBACKUP = "VbrBackup"

    def __str__(self) -> str:
        return str(self.value)
