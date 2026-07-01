from enum import Enum


class SqlRestorePointExpansion(str, Enum):
    ACCOUNTSINFO = "AccountsInfo"
    NONE = "None"
    REPOSITORYNAME = "RepositoryName"
    STORAGETIER = "StorageTier"
    VBRBACKUP = "VbrBackup"

    def __str__(self) -> str:
        return str(self.value)
