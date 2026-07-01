from enum import Enum


class VnetPolicyExpansion(str, Enum):
    ALL = "All"
    LASTBACKUPCOPYSESSION = "LastBackupCopySession"
    LASTBACKUPSESSION = "LastBackupSession"
    NONE = "None"
    TARGETREPOSITORY = "TargetRepository"

    def __str__(self) -> str:
        return str(self.value)
