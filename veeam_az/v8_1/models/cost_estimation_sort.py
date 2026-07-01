from enum import Enum


class CostEstimationSort(str, Enum):
    ARCHIVECOSTASC = "ArchiveCostAsc"
    ARCHIVECOSTDESC = "ArchiveCostDesc"
    BACKUPCOSTASC = "BackupCostAsc"
    BACKUPCOSTDESC = "BackupCostDesc"
    SNAPSHOTCOSTASC = "SnapshotCostAsc"
    SNAPSHOTCOSTDESC = "SnapshotCostDesc"
    TOTALASC = "TotalAsc"
    TOTALDESC = "TotalDesc"
    TRAFFICCOSTASC = "TrafficCostAsc"
    TRAFFICCOSTDESC = "TrafficCostDesc"
    TRANSACTIONCOSTASC = "TransactionCostAsc"
    TRANSACTIONCOSTDESC = "TransactionCostDesc"
    VIRTUALMACHINENAMEASC = "VirtualMachineNameAsc"
    VIRTUALMACHINENAMEDESC = "VirtualMachineNameDesc"

    def __str__(self) -> str:
        return str(self.value)
