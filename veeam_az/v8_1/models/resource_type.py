from enum import Enum


class ResourceType(str, Enum):
    FILESHARE = "FileShare"
    GREMLINCOSMOSACCOUNT = "GremlinCosmosAccount"
    KEYVAULT = "KeyVault"
    MANAGEDDATABASE = "ManagedDatabase"
    MANAGEDDISK = "ManagedDisk"
    MONGODBCOSMOSACCOUNT = "MongoDbCosmosAccount"
    NETWORKSECURITYGROUP = "NetworkSecurityGroup"
    NOSQLCOSMOSACCOUNT = "NoSqlCosmosAccount"
    POSTGRESCOSMOSACCOUNT = "PostgresCosmosAccount"
    REGION = "Region"
    RESOURCEGROUP = "ResourceGroup"
    SQLELASTICPOOL = "SqlElasticPool"
    SQLSERVER = "SqlServer"
    SQLSERVERMANAGEDINSTANCE = "SqlServerManagedInstance"
    STORAGEACCOUNT = "StorageAccount"
    SUBSCRIPTION = "Subscription"
    TABLECOSMOSACCOUNT = "TableCosmosAccount"
    UNKNOWN = "Unknown"
    UNMANAGEDATTACHEDDISK = "UnmanagedAttachedDisk"
    UNMANAGEDDATABASE = "UnmanagedDatabase"
    UNMANAGEDDETACHEDDISK = "UnmanagedDetachedDisk"
    VIRTUALMACHINE = "VirtualMachine"
    VIRTUALNETWORK = "VirtualNetwork"

    def __str__(self) -> str:
        return str(self.value)
