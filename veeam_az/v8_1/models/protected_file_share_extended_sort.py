from enum import Enum


class ProtectedFileShareExtendedSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    POLICYASC = "PolicyAsc"
    POLICYDESC = "PolicyDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    RESTOREPOINTCOUNTASC = "RestorePointCountAsc"
    RESTOREPOINTCOUNTDESC = "RestorePointCountDesc"
    SIZEASC = "SizeAsc"
    SIZEDESC = "SizeDesc"
    STORAGEACCOUNTASC = "StorageAccountAsc"
    STORAGEACCOUNTDESC = "StorageAccountDesc"
    SUBSCRIPTIONIDASC = "SubscriptionIdAsc"
    SUBSCRIPTIONIDDESC = "SubscriptionIdDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"

    def __str__(self) -> str:
        return str(self.value)
