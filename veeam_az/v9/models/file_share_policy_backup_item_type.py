from enum import Enum


class FileSharePolicyBackupItemType(str, Enum):
    FILESHARE = "FileShare"
    RESOURCEGROUP = "ResourceGroup"
    STORAGEACCOUNT = "StorageAccount"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
