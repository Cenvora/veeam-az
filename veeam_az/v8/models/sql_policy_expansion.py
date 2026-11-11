from enum import Enum


class SqlPolicyExpansion(str, Enum):
    ALL = "All"
    EXCLUDEDRESOURCES = "ExcludedResources"
    LASTBACKUPSESSION = "LastBackupSession"
    LASTFINISHEDBACKUPSESSION = "LastFinishedBackupSession"
    NONE = "None"
    PROTECTEDRESOURCES = "ProtectedResources"
    REGIONS = "Regions"
    REPOSITORY = "Repository"
    STAGINGSERVERS = "StagingServers"

    def __str__(self) -> str:
        return str(self.value)
