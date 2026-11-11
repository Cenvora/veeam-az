from enum import Enum


class HealthCheckJobCheckedItemsSort(str, Enum):
    CORRUPTEDRESTOREPOINTSASC = "CorruptedRestorePointsAsc"
    CORRUPTEDRESTOREPOINTSDESC = "CorruptedRestorePointsDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    RESOURCENAMEASC = "ResourceNameAsc"
    RESOURCENAMEDESC = "ResourceNameDesc"
    TOTALRESTOREPOINTSASC = "TotalRestorePointsAsc"
    TOTALRESTOREPOINTSDESC = "TotalRestorePointsDesc"

    def __str__(self) -> str:
        return str(self.value)
