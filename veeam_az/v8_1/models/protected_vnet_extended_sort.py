from enum import Enum


class ProtectedVnetExtendedSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    REGIONCOUNTASC = "RegionCountAsc"
    REGIONCOUNTDESC = "RegionCountDesc"
    RESTOREPOINTCOUNTASC = "RestorePointCountAsc"
    RESTOREPOINTCOUNTDESC = "RestorePointCountDesc"
    SUBSCRIPTIONIDASC = "SubscriptionIdAsc"
    SUBSCRIPTIONIDDESC = "SubscriptionIdDesc"
    SUBSCRIPTIONNAMEASC = "SubscriptionNameAsc"
    SUBSCRIPTIONNAMEDESC = "SubscriptionNameDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"
    TENANTNAMEASC = "TenantNameAsc"
    TENANTNAMEDESC = "TenantNameDesc"

    def __str__(self) -> str:
        return str(self.value)
