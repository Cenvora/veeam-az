from enum import Enum


class FileSharePolicyExpansion(str, Enum):
    ALL = "All"
    EXCLUDEDRESOURCES = "ExcludedResources"
    LASTBACKUPSESSION = "LastBackupSession"
    LASTFINISHEDBACKUPSESSION = "LastFinishedBackupSession"
    NONE = "None"
    PROTECTEDRESOURCES = "ProtectedResources"
    REGIONS = "Regions"

    def __str__(self) -> str:
        return str(self.value)
