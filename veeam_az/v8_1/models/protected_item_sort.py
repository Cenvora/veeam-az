from enum import Enum


class ProtectedItemSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    OSTYPEASC = "OsTypeAsc"
    OSTYPEDESC = "OsTypeDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    VMSIZEASC = "VmSizeAsc"
    VMSIZEDESC = "VmSizeDesc"

    def __str__(self) -> str:
        return str(self.value)
