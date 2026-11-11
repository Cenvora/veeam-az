from enum import Enum


class RepositoryType(str, Enum):
    BACKUP = "Backup"
    UNKNOWN = "Unknown"
    VEEAMVAULT = "VeeamVault"

    def __str__(self) -> str:
        return str(self.value)
