from enum import Enum


class BackupJobProtectedItemsSort(str, Enum):
    FAILEDASC = "FailedAsc"
    FAILEDDESC = "FailedDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    RESOURCENAMEASC = "ResourceNameAsc"
    RESOURCENAMEDESC = "ResourceNameDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBSCRIPTIONASC = "SubscriptionAsc"
    SUBSCRIPTIONDESC = "SubscriptionDesc"
    SUCCEEDEDASC = "SucceededAsc"
    SUCCEEDEDDESC = "SucceededDesc"

    def __str__(self) -> str:
        return str(self.value)
