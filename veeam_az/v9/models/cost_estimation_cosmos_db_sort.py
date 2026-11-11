from enum import Enum


class CostEstimationCosmosDbSort(str, Enum):
    BACKUPCOSTASC = "BackupCostAsc"
    BACKUPCOSTDESC = "BackupCostDesc"
    CONTINUOUSBACKUPCOSTASC = "ContinuousBackupCostAsc"
    CONTINUOUSBACKUPCOSTDESC = "ContinuousBackupCostDesc"
    RESOURCENAMEASC = "ResourceNameAsc"
    RESOURCENAMEDESC = "ResourceNameDesc"
    TOTALASC = "TotalAsc"
    TOTALDESC = "TotalDesc"
    TRAFFICCOSTASC = "TrafficCostAsc"
    TRAFFICCOSTDESC = "TrafficCostDesc"
    TRANSACTIONCOSTASC = "TransactionCostAsc"
    TRANSACTIONCOSTDESC = "TransactionCostDesc"

    def __str__(self) -> str:
        return str(self.value)
