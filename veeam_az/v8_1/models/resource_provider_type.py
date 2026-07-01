from enum import Enum


class ResourceProviderType(str, Enum):
    COSMOSDB = "CosmosDb"
    SQLMANAGEDINSTANCE = "SqlManagedInstance"
    SQLSERVER = "SqlServer"
    STORAGEACCOUNT = "StorageAccount"
    UNKNOWN = "Unknown"
    VIRTUALMACHINE = "VirtualMachine"
    VIRTUALNETWORK = "VirtualNetwork"

    def __str__(self) -> str:
        return str(self.value)
