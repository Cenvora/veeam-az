from enum import Enum


class PolicyExpansion(str, Enum):
    ALL = "All"
    EXCLUDEDRESOURCES = "ExcludedResources"
    LASTBACKUPSESSION = "LastBackupSession"
    LASTFINISHEDBACKUPSESSION = "LastFinishedBackupSession"
    NONE = "None"
    PROTECTEDRESOURCES = "ProtectedResources"
    REGIONS = "Regions"
    REPOSITORY = "Repository"
    TAGGROUPS = "TagGroups"

    def __str__(self) -> str:
        return str(self.value)
