from enum import Enum


class VnetRestorePointResourcesReportSort(str, Enum):
    MODIFICATIONDATEASC = "ModificationDateAsc"
    MODIFICATIONDATEDESC = "ModificationDateDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEIDASC = "ResourceIdAsc"
    RESOURCEIDDESC = "ResourceIdDesc"
    RESOURCENAMEASC = "ResourceNameAsc"
    RESOURCENAMEDESC = "ResourceNameDesc"
    STATEASC = "StateAsc"
    STATEDESC = "StateDesc"
    TYPEASC = "TypeAsc"
    TYPEDESC = "TypeDesc"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
