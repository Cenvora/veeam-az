from enum import Enum


class RepositoryExpansion(str, Enum):
    ALL = "All"
    AZUREACCOUNT = "AzureAccount"
    KEYVAULT = "KeyVault"
    NONE = "None"
    REGION = "Region"
    STORAGEACCOUNT = "StorageAccount"
    USEDSPACE = "UsedSpace"

    def __str__(self) -> str:
        return str(self.value)
