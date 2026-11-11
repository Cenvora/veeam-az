from enum import Enum


class WorkerSort(str, Enum):
    INSTANCETYPEASC = "InstanceTypeAsc"
    INSTANCETYPEDESC = "InstanceTypeDesc"
    IPASC = "IpAsc"
    IPDESC = "IpDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    NETWORKASC = "NetworkAsc"
    NETWORKDESC = "NetworkDesc"
    PURPOSEASC = "PurposeAsc"
    PURPOSEDESC = "PurposeDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"

    def __str__(self) -> str:
        return str(self.value)
