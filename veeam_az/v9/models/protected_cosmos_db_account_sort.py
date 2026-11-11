from enum import Enum


class ProtectedCosmosDbAccountSort(str, Enum):
    ACCOUNTTYPEASC = "AccountTypeAsc"
    ACCOUNTTYPEDESC = "AccountTypeDesc"
    ARCHIVESIZEBYTESASC = "ArchiveSizeBytesAsc"
    ARCHIVESIZEBYTESDESC = "ArchiveSizeBytesDesc"
    BACKUPSIZEBYTESASC = "BackupSizeBytesAsc"
    BACKUPSIZEBYTESDESC = "BackupSizeBytesDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LATESTBACKUPASC = "LatestBackupAsc"
    LATESTBACKUPDESC = "LatestBackupDesc"
    LATESTRESTORABLETIMESTAMPASC = "LatestRestorableTimestampAsc"
    LATESTRESTORABLETIMESTAMPDESC = "LatestRestorableTimestampDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    POLICYASC = "PolicyAsc"
    POLICYDESC = "PolicyDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    RESTOREPOINTSCOUNTASC = "RestorePointsCountAsc"
    RESTOREPOINTSCOUNTDESC = "RestorePointsCountDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBSCRIPTIONNAMEASC = "SubscriptionNameAsc"
    SUBSCRIPTIONNAMEDESC = "SubscriptionNameDesc"
    TENANTNAMEASC = "TenantNameAsc"
    TENANTNAMEDESC = "TenantNameDesc"

    def __str__(self) -> str:
        return str(self.value)
