from enum import Enum


class WorkloadType(str, Enum):
    COSMOSDB = "CosmosDb"
    FILESHARES = "FileShares"
    SQL = "SQL"
    VIRTUALMACHINE = "VirtualMachine"
    VIRTUALNETWORK = "VirtualNetwork"
    WORKLOADINDEPENDENT = "WorkloadIndependent"

    def __str__(self) -> str:
        return str(self.value)
