from enum import Enum


class AzureAccountPurpose(str, Enum):
    AZUREFILES = "AzureFiles"
    AZURESQLBACKUP = "AzureSqlBackup"
    AZURESQLRESTORE = "AzureSqlRestore"
    COSMOSBACKUP = "CosmosBackup"
    COSMOSRESTORE = "CosmosRestore"
    NONE = "None"
    REPOSITORY = "Repository"
    UNKNOWN = "Unknown"
    VIRTUALMACHINEBACKUP = "VirtualMachineBackup"
    VIRTUALMACHINERESTORE = "VirtualMachineRestore"
    VNETBACKUP = "VnetBackup"
    VNETRESTORE = "VnetRestore"
    WORKERMANAGEMENT = "WorkerManagement"

    def __str__(self) -> str:
        return str(self.value)
