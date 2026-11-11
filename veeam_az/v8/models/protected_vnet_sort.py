from enum import Enum


class ProtectedVnetSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    SUBSCRIPTIONIDASC = "SubscriptionIdAsc"
    SUBSCRIPTIONIDDESC = "SubscriptionIdDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"

    def __str__(self) -> str:
        return str(self.value)
