from enum import Enum


class DatabaseSort(str, Enum):
    ACCOUNTASC = "AccountAsc"
    ACCOUNTDESC = "AccountDesc"
    BACKUPPOLICYASC = "BackupPolicyAsc"
    BACKUPPOLICYDESC = "BackupPolicyDesc"
    ENCRYPTIONASC = "EncryptionAsc"
    ENCRYPTIONDESC = "EncryptionDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    RESTOREPOINTSASC = "RestorePointsAsc"
    RESTOREPOINTSDESC = "RestorePointsDesc"
    SERVERNAMEASC = "ServerNameAsc"
    SERVERNAMEDESC = "ServerNameDesc"
    SIZEASC = "SizeAsc"
    SIZEDESC = "SizeDesc"
    SQLELASTICPOOLASC = "SqlElasticPoolAsc"
    SQLELASTICPOOLDESC = "SqlElasticPoolDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBSCRIPTIONIDASC = "SubscriptionIdAsc"
    SUBSCRIPTIONIDDESC = "SubscriptionIdDesc"
    SUBSCRIPTIONNAMEASC = "SubscriptionNameAsc"
    SUBSCRIPTIONNAMEDESC = "SubscriptionNameDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"

    def __str__(self) -> str:
        return str(self.value)
