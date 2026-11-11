from enum import Enum


class ProtectedFileShareSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"

    def __str__(self) -> str:
        return str(self.value)
