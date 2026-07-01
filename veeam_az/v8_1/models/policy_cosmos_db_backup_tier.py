from enum import Enum


class PolicyCosmosDbBackupTier(str, Enum):
    CONTINUOUS30DAYS = "Continuous30Days"
    CONTINUOUS7DAYS = "Continuous7Days"

    def __str__(self) -> str:
        return str(self.value)
