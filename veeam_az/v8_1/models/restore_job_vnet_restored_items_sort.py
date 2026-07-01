from enum import Enum


class RestoreJobVnetRestoredItemsSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBSCRIPTIONASC = "SubscriptionAsc"
    SUBSCRIPTIONDESC = "SubscriptionDesc"

    def __str__(self) -> str:
        return str(self.value)
