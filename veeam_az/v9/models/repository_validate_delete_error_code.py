from enum import Enum


class RepositoryValidateDeleteErrorCode(str, Enum):
    HASACTIVEDATARETRIEVALTASK = "HasActiveDataRetrievalTask"
    UNKNOWN = "Unknown"
    USEDINCONFIGURATIONBACKUPSETTING = "UsedInConfigurationBackupSetting"

    def __str__(self) -> str:
        return str(self.value)
