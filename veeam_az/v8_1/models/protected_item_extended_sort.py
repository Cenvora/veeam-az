from enum import Enum


class ProtectedItemExtendedSort(str, Enum):
    ARCHIVESIZEASC = "ArchiveSizeAsc"
    ARCHIVESIZEDESC = "ArchiveSizeDesc"
    BACKUPSIZEASC = "BackupSizeAsc"
    BACKUPSIZEDESC = "BackupSizeDesc"
    DATARETRIEVALSTATUSASC = "DataRetrievalStatusAsc"
    DATARETRIEVALSTATUSDESC = "DataRetrievalStatusDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    OSTYPEASC = "OsTypeAsc"
    OSTYPEDESC = "OsTypeDesc"
    POLICYASC = "PolicyAsc"
    POLICYDESC = "PolicyDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    RESTOREPOINTCOUNTASC = "RestorePointCountAsc"
    RESTOREPOINTCOUNTDESC = "RestorePointCountDesc"
    SUBSCRIPTIONIDASC = "SubscriptionIdAsc"
    SUBSCRIPTIONIDDESC = "SubscriptionIdDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"
    VMSIZEASC = "VmSizeAsc"
    VMSIZEDESC = "VmSizeDesc"

    def __str__(self) -> str:
        return str(self.value)
