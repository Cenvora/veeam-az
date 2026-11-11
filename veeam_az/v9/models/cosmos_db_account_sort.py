from enum import Enum


class CosmosDbAccountSort(str, Enum):
    ACCOUNTTYPEASC = "AccountTypeAsc"
    ACCOUNTTYPEDESC = "AccountTypeDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTESTBACKUPASC = "LastestBackupAsc"
    LASTESTBACKUPDESC = "LastestBackupDesc"
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
    SOURCESIZEASC = "SourceSizeAsc"
    SOURCESIZEDESC = "SourceSizeDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBSCRIPTIONNAMEASC = "SubscriptionNameAsc"
    SUBSCRIPTIONNAMEDESC = "SubscriptionNameDesc"

    def __str__(self) -> str:
        return str(self.value)
