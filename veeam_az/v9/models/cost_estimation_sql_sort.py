from enum import Enum


class CostEstimationSqlSort(str, Enum):
    BACKUPCOSTASC = "BackupCostAsc"
    BACKUPCOSTDESC = "BackupCostDesc"
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
