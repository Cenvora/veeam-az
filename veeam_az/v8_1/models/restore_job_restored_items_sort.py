from enum import Enum


class RestoreJobRestoredItemsSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"

    def __str__(self) -> str:
        return str(self.value)
