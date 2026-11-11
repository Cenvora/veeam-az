from enum import Enum


class PolicyType(str, Enum):
    AZURESQL = "AzureSql"
    COSMOSDB = "CosmosDb"
    FILESHARES = "FileShares"
    PROTECTIONVMPOLICY = "ProtectionVmPolicy"
    UNKNOWN = "Unknown"
    VIRTUALMACHINES = "VirtualMachines"
    VNET = "Vnet"

    def __str__(self) -> str:
        return str(self.value)
