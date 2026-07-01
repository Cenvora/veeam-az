from enum import Enum


class LicensedResourceSort(str, Enum):
    INSTANCESASC = "InstancesAsc"
    INSTANCESDESC = "InstancesDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    RESOURCETYPEASC = "ResourceTypeAsc"
    RESOURCETYPEDESC = "ResourceTypeDesc"
    STATEASC = "StateAsc"
    STATEDESC = "StateDesc"

    def __str__(self) -> str:
        return str(self.value)
