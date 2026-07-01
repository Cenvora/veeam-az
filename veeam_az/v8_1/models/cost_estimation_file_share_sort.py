from enum import Enum


class CostEstimationFileShareSort(str, Enum):
    RESOURCENAMEASC = "ResourceNameAsc"
    RESOURCENAMEDESC = "ResourceNameDesc"
    SNAPSHOTCOSTASC = "SnapshotCostAsc"
    SNAPSHOTCOSTDESC = "SnapshotCostDesc"
    TOTALASC = "TotalAsc"
    TOTALDESC = "TotalDesc"

    def __str__(self) -> str:
        return str(self.value)
