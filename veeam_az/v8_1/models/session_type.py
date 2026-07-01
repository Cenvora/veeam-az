from enum import Enum


class SessionType(str, Enum):
    CONFIGURATIONBACKUP = "ConfigurationBackup"
    COSMOSDBCONFIGURATION = "CosmosDbConfiguration"
    DELETION = "Deletion"
    FILELEVELRESTORE = "FileLevelRestore"
    FILESHAREINDEXING = "FileShareIndexing"
    HEALTHCHECK = "HealthCheck"
    INFRASTRUCTURERESCAN = "InfrastructureRescan"
    MANUALBACKUP = "ManualBackup"
    MANUALSNAPSHOT = "ManualSnapshot"
    POLICYARCHIVE = "PolicyArchive"
    POLICYBACKUP = "PolicyBackup"
    POLICYSNAPSHOT = "PolicySnapshot"
    REPOSITORYTASKS = "RepositoryTasks"
    RESTORE = "Restore"
    RETENTION = "Retention"

    def __str__(self) -> str:
        return str(self.value)
